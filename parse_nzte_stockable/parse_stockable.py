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
scope_header = 'Scope'
content_header = 'Does the data contain diagnoses and clinical outcomes?\nDoes the data contain procedures, device information and medication for therapy?\nDoes this data set have cost / price data?'
dictionary_header = 'Presence of Data dictionary? Column headings in Excel or any kind of data model if residing in a relational database (e.g. Access, SQL Server, Oracle etc.) '
linkage_header = 'Linked (or linkable) to other datasets within your organisation or across the Sector'
update_header = 'How often does this data set get updated? Daily? Weekly? Monthly? Quarterly? Yearly?'
quality_header = 'Indication of data quality (e.g. missing values, duplications, inconsistencies etc.). Q: Audits? How do you ensure the data is valid and correct?'
collection_header = 'Brief info about the systems and processes used to collect/manage data. Q: Where the data is collected, in what form, and accessibility?'
format_header = 'Data format, e.g., data structure, data types, and storage form (relational database, Excel, csv, etc.).'
structure_header = 'How well the data is structured, e.g. free text VS coded text VS pick-list (drop-down list)'
availability_header = 'How quickly can the data be made available from time of request and how old is the data once it is made available'

for row in stockable.iterrows():
  line = row[1]
  if line['DB_Custodian_Org'] in ['MoH', 'ADHB', 'CMDHB', 'Southern DHB', 'Waikato DHB', 'WDHB']:
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
      template.content = ''
      # add other information when available
      if not isinstance(line[description_header], float):
        template.content += '\n <h4> <u>Description:</u> </h4>' + '\n' + str(line[description_header])
        template['description'] = str(line[description_header])
      template.content += '\n <h4> <u>Additional information:</u> </h4>' + '\n <table style="border: 1px solid">'
      if not isinstance(line[nhi_header], float):
        template.content += '\n <tr> <td width="40%">' + nhi_header + '</td> <td>' + str(line[nhi_header]) + '</td> </tr>'
      if not isinstance(line[phi_header], float):
        template.content += '\n <tr> <td width="40%">' + phi_header + '</td> <td>' + str(line[phi_header]) + '</td> </tr>'
      if not isinstance(line[volume_header], float):
        template.content += '\n <tr> <td width="40%">' + volume_header + '</td> <td>' + str(line[volume_header]) + '</td> </tr>'
      if not isinstance(line[access_header], float):
        template.content += '\n <tr> <td width="40%">' + access_header + '</td> <td>' + str(line[access_header]) + '</td> </tr>'
      if not isinstance(line[scope_header], float):
        template.content += '\n <tr> <td width="40%">' + scope_header + '</td> <td>' + str(line[scope_header]) + '</td> </tr>'
      if not isinstance(line[content_header], float):
        template.content += '\n <tr> <td width="40%">' + content_header + '</td> <td>' + str(line[content_header]) + '</td> </tr>'
      if not isinstance(line[dictionary_header], float):
        template.content += '\n <tr> <td width="40%">' + dictionary_header + '</td> <td>' + str(line[dictionary_header]) + '</td> </tr>'
      if not isinstance(line[linkage_header], float):
        template.content += '\n <tr> <td width="40%">' + linkage_header + '</td> <td>' + str(line[linkage_header]) + '</td> </tr>'
      if not isinstance(line[update_header], float):
        template.content += '\n <tr> <td width="40%">' + update_header + '</td> <td>' + str(line[update_header]) + '</td> </tr>'
      if not isinstance(line[quality_header], float):
        template.content += '\n <tr> <td width="40%">' + quality_header + '</td> <td>' + str(line[quality_header]) + '</td> </tr>'
      if not isinstance(line[collection_header], float):
        template.content += '\n <tr> <td width="40%">' + collection_header + '</td> <td>' + str(line[collection_header]) + '</td> </tr>'
      if not isinstance(line[format_header], float):
        template.content += '\n <tr> <td width="40%">' + format_header + '</td> <td>' + str(line[format_header]) + '</td> </tr>'
      if not isinstance(line[structure_header], float):
        template.content += '\n <tr> <td width="40%">' + structure_header + '</td> <td>' + str(line[structure_header]) + '</td> </tr>'
      if not isinstance(line[availability_header], float):
        template.content += '\n <tr> <td width="40%">' + availability_header + '</td> <td>' + str(line[availability_header]) + '</td> </tr>'
      template.content += '\n </table>'
      # write the post
      frontmatter.dump(template, f_out)  

            


      

