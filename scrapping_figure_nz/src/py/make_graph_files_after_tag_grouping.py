import csv, sys, shutil, os, unidecode
import pandas as pd

print("parsing", sys.argv[1])

def clean(x):
    # neo4j-import doesn't support: multiline (coming soon), quotes next to each other and escape quotes with '\""'
    return x.replace('\n','').replace('\r','').replace('\\','').replace('"','')

def open_csv(name):
    return csv.writer(open('../../resources/neo4j_in_tag_grouping/{}.csv'.format(name), 'w'), doublequote=False, escapechar='\\')

try:
    shutil.rmtree('../../resources/neo4j_in_tag_grouping')
except:
    pass
os.mkdir('../../resources/neo4j_in_tag_grouping')


# nodes csvs
providers = open_csv('_providers')
datasets = open_csv('_datasets')
titles = open_csv('_titles')
subtitles = open_csv('_subtitles')
tags = open_csv('_tags')

# edges csvs
provider_dataset_rel = open_csv('_provider_dataset_rel')
dataset_tag_rel = open_csv('_dataset_tag_rel')
tag_title_rel = open_csv('_tag_title_rel')
title_subtitle_rel = open_csv('_title_subtitle_rel')
dataset_title_rel = open_csv('_dataset_title_rel')

# headers
providers.writerow(['providerId:ID(Provider)', 'name', ':LABEL'])
datasets.writerow(['datasetId:ID(Dataset)', 'name', ':LABEL'])
titles.writerow(['titleId:ID(Title)', 'name', 'url', ':LABEL'])
subtitles.writerow(['subtitleId:ID(Subtitle)', 'name', 'url', ':LABEL'])
tags.writerow(['tagId:ID(Tag)', 'name', ':LABEL'])
provider_dataset_rel.writerow([':START_ID(Provider)', ':END_ID(Dataset)']) # provides
dataset_tag_rel.writerow([':START_ID(Dataset)', ':END_ID(Tag)']) # has_information_about
dataset_title_rel.writerow([':START_ID(Dataset)', ':END_ID(Title)']) # is_used_in
tag_title_rel.writerow([':START_ID(Tag)', ':END_ID(Title)']) # is_described_in
title_subtitle_rel.writerow([':START_ID(Title)', ':END_ID(Subtitle)']) # is_specified_in

lkup = pd.read_csv("../../resources/lkup_final.csv")

with open(sys.argv[1], 'r') as f:
    reader = csv.DictReader(f)
    headers = reader.fieldnames
    for line in reader:
        provider_id = line['provider']; provider_name = line['provider']
        dataset_id = hash(line['dataset']); dataset_name = line['dataset']
        providers.writerow([provider_id, provider_name, 'Provider'])
        datasets.writerow([dataset_id, dataset_name, 'Dataset'])
        provider_dataset_rel.writerow([provider_id, dataset_id])
        if len(line['title']) > 0 :
          title_id = hash(line['title']); title_name = line['title']
          subtitle_id = hash(title_name + '-' + line['subtitle']); subtitle_name = line['subtitle']
          subtitles.writerow([subtitle_id, subtitle_name, line['url'], 'Subtitle'])
          title_subtitle_rel.writerow([title_id, subtitle_id])
        else:
          title_id = hash(line['name']); title_name = line['name']
        dataset_title_rel.writerow([dataset_id, title_id])
        titles.writerow([title_id, title_name, '' if len(line['subtitle']) > 0  else line['url'], 'Title'])
        for tag in line['tags'].split('|'):
            if len(tag) > 0 and tag != 'tags': # scrappy seems to include the header in the csv output sometimes.. bug to raise?
                tag = unidecode.unidecode(tag).upper().strip()
                tag = lkup.new[lkup.tag==tag].tolist()[0]
                tag_id = tag; tag_name = tag
                tags.writerow([tag_id, tag_name, 'Tag'])
                dataset_tag_rel.writerow([dataset_id, tag_id])
                tag_title_rel.writerow([tag_id, title_id])
            
