import frontmatter
import pandas as pd
import copy
from datetime import datetime
import json

stockable = pd.read_excel('figure_nz_for_jekyll.xlsx')

with open('dummy.md') as f_dummy:
  dummy = frontmatter.load(f_dummy)

description_header = 'Purpose and description of dataset'

for row in stockable.iterrows():
  line = row[1]
  template = copy.copy(dummy)
  dataset_fmt_name = ''.join(e for e in line['DataSet(s)'].lower() if e.isalnum() or e == ' ')
  f_dataset_name = datetime.now().strftime("%Y-%m-%d") + '-' + dataset_fmt_name.replace(" ", "-") + '.md'
  with open('posts/' + f_dataset_name, 'wb') as f_out:
    # update the yaml file properties
    template['date'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    template['title'] = line['DataSet(s)']
    template['id'] = dataset_fmt_name.replace(" ", "_")
    template['provider'] = line['provider']
    template['link'] = line['link']
    template['categories'] = line['categories']
    template['tags'] = line['tags'].split("|")
    template['figure_nz'] = json.loads(line['figure_nz'])
    # write the post
    frontmatter.dump(template, f_out)  

            


      

