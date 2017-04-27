import csv, sys, shutil, os

print("parsing", sys.argv[1])

def clean(x):
    # neo4j-import doesn't support: multiline (coming soon), quotes next to each other and escape quotes with '\""'
    return x.replace('\n','').replace('\r','').replace('\\','').replace('"','')

def open_csv(name):
    return csv.writer(open('../../resources/neo4j_in/{}.csv'.format(name), 'w'), doublequote=False, escapechar='\\')

try:
    shutil.rmtree('../../resources/neo4j_in')
except:
    pass
os.mkdir('../../resources/neo4j_in')


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
titles.writerow(['titleId:ID(Title)', 'name', ':LABEL'])
subtitles.writerow(['subtitleId:ID(Subtitle)', 'name', ':LABEL'])
tags.writerow(['tagId:ID(Tag)', 'name', ':LABEL'])
provider_dataset_rel.writerow([':START_ID(Provider)', ':END_ID(Dataset)']) # provides
dataset_tag_rel.writerow([':START_ID(Dataset)', ':END_ID(Tag)']) # has_information_about
dataset_title_rel.writerow([':START_ID(Dataset)', ':END_ID(Title)']) # is_used_in
tag_title_rel.writerow([':START_ID(Tag)', ':END_ID(Title)']) # is_described_in
title_subtitle_rel.writerow([':START_ID(Title)', ':END_ID(Subtitle)']) # is_specified_in


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
          subtitles.writerow([subtitle_id, subtitle_name, 'Subtitle'])
          title_subtitle_rel.writerow([title_id, subtitle_id])
        else:
          title_id = hash(line['name']); title_name = line['name']
        dataset_title_rel.writerow([dataset_id, title_id])
        titles.writerow([title_id, title_name, 'Title'])
        for tag in line['tags'].split('|'):
            if len(tag) > 0 :
                tag_id = tag; tag_name = tag
                tags.writerow([tag_id, tag_name, 'Tag'])
                dataset_tag_rel.writerow([dataset_id, tag_id])
                tag_title_rel.writerow([tag_id, title_id])
            
