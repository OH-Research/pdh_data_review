import frontmatter
import pandas as pd
import copy
from datetime import datetime

stockable = pd.read_excel('_Appendix.C_Full.detail.stocktake.xlsx')

with open('dummy.md') as f_dummy:
  dummy = frontmatter.load(f_dummy)

description_header = 'Purpose and description of dataset'
nhi_header = 'Have_(encrypted)_NHI'
phi_header = 'Personally identifiable (e.g. linked to NHI numbers) and longitudinal or aggregated (e.g. for planning, clinical research etc.)?'
volume_header = 'Volume of data (e.g. how many records)\nSince when?'
access_header = 'Purpose and governance including ethics committee/patient consent mechanisms. Q: How do you get around ethics/privacy issues with your data sources? Esp. DHBs?'

for row in stockable.iterrows():
  line = row[1]
  if line['DB_Custodian_Org'] in ['MoH', 'ADHB', 'CMDHB', 'Southern DHB', 'Waikato DHB', 'WDHB']:
    template = copy.copy(dummy)
    dataset_fmt_name = ''.join(e for e in line['DataSet(s)'].lower() if e.isalnum() or e == ' ')
    f_dataset_name = datetime.now().strftime("%Y-%m-%d") + '-' + dataset_fmt_name.replace(" ", "-") + '.md'
    with open('posts/' + f_dataset_name, 'wb') as f_out:
      template['date'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
      template['title'] = line['DataSet(s)']
      template['id'] = dataset_fmt_name.replace(" ", "_")
      template['provider'] = line['provider']
      template['link'] = line['link']
      template['categories'] = line['categories']
      template['tags'] = line['tags'].split("|")
      template.content = ''

      # add dataset description
      if not isinstance(line[description_header], float):
        template.content += '\n <h4> <u>Description:</u> </h4>' + '\n' + str(line[description_header])

      # add other information when available
      template.content += '\n <h4> <u>Additional information:</u> </h4>' + '\n <table style="border: 1px solid">'
      if not isinstance(line[nhi_header], float):
        template.content += '\n <tr> <td width="40%"> Does it contain (encrypted) NHI? </td> <td>' + str(line[nhi_header]) + '</td> </tr>'
      if not isinstance(line[phi_header], float):
      	template.content += '\n <tr> <td width="40%"> Is it personally identifiable? </td> <td>' + str(line[phi_header]) + '</td> </tr>'
      if not isinstance(line[volume_header], float):
      	template.content += '\n <tr> <td width="40%"> Information about the volume: </td> <td>' + str(line[volume_header]) + '</td> </tr>'
      if not isinstance(line[access_header], float):
      	template.content += '\n <tr> <td width="40%"> Access conditions: </td> <td>' + str(line[access_header]) + '</td> </tr>'
      template.content += '\n </table>'

      # write the post
      frontmatter.dump(template, f_out)  

            


      

