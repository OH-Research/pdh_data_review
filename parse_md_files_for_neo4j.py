import os
import pandas as pd
import frontmatter
import argparse

def main(folder_in, folder_out):
  provider_df = pd.DataFrame({'providerId:ID(Provider)': [], 'name': [], ':LABEL': []})
  dataset_df = pd.DataFrame({'datasetId:ID(Dataset)': [], 'name': [], ':LABEL': []})
  tag_df = pd.DataFrame({'tagId:ID(Tag)': [], 'name': [], ':LABEL': []})
  category_df = pd.DataFrame({'categoryId:ID(Category)': [], 'name': [], ':LABEL': []})
  level1_df = pd.DataFrame({'level1Id:ID(Level1)': [], 'name': [], ':LABEL': []})

  provider_dataset_df =  pd.DataFrame({':START_ID(Provider)': [], ':END_ID(Dataset)': []})
  dataset_tag_df =  pd.DataFrame({':START_ID(Dataset)': [], ':END_ID(Tag)': []})
  dataset_category_df =  pd.DataFrame({':START_ID(Dataset)': [], ':END_ID(Category)': []})
  provider_category_df =  pd.DataFrame({':START_ID(Provider)': [], ':END_ID(Category)': []})
  dataset_level1_df =  pd.DataFrame({':START_ID(Dataset)': [], ':END_ID(Level1)': []})

  for filename in os.listdir(folder_in):
    if filename.endswith(".md"): 
      with open(os.path.join(folder_in, filename)) as f:
        dataset_info = frontmatter.load(f)
        dataset_node_id = str(hash(dataset_info['id']))
        provider_node_id = str(hash(dataset_info['provider']))
        provider_df = pd.concat([provider_df, pd.DataFrame({'providerId:ID(Provider)': [provider_node_id], 'name': [dataset_info['provider']], ':LABEL': ['Provider']})], ignore_index=True)
        dataset_df = pd.concat([dataset_df, pd.DataFrame({'datasetId:ID(Dataset)': [dataset_node_id], 'name': [dataset_info['title']], ':LABEL': ['Dataset']})], ignore_index=True)
        provider_dataset_df = pd.concat([provider_dataset_df, pd.DataFrame({':START_ID(Provider)': [provider_node_id], ':END_ID(Dataset)': [dataset_node_id]})], ignore_index=True)
        for tag in dataset_info['tags']:
          tag_node_id = str(hash(tag))
          tag_df = pd.concat([tag_df, pd.DataFrame({'tagId:ID(Tag)': [tag_node_id], 'name': [tag], ':LABEL': ['Tag']})], ignore_index=True)
          dataset_tag_df = pd.concat([dataset_tag_df, pd.DataFrame({':START_ID(Dataset)': [dataset_node_id], ':END_ID(Tag)': [tag_node_id]})], ignore_index=True)
        for category in dataset_info['categories'].split():
          category_node_id = str(hash(category))
          category_df = pd.concat([category_df, pd.DataFrame({'categoryId:ID(Category)': [category_node_id], 'name': [category], ':LABEL': ['Category']})], ignore_index=True)
          dataset_category_df = pd.concat([dataset_category_df, pd.DataFrame({':START_ID(Dataset)': [dataset_node_id], ':END_ID(Category)': [category_node_id]})], ignore_index=True)
          provider_category_df = pd.concat([provider_category_df, pd.DataFrame({':START_ID(Provider)': [provider_node_id], ':END_ID(Category)': [category_node_id]})], ignore_index=True)
        if 'figure_nz' in dataset_info.keys():
          for item in dataset_info['figure_nz']:
            level1_node_id = str(hash(item['title_l1']))
            level1_df = pd.concat([level1_df, pd.DataFrame({'level1Id:ID(Level1)': [level1_node_id], 'name': [item['title_l1']], ':LABEL': ['Level1']})], ignore_index=True)
            dataset_level1_df = pd.concat([dataset_level1_df, pd.DataFrame({':START_ID(Dataset)': [dataset_node_id], ':END_ID(Level1)': [level1_node_id]})], ignore_index=True)
   
    else:
      pass

  if not os.path.exists(folder_out):
      os.makedirs(folder_out)

  provider_df.drop_duplicates().reset_index(drop=True).to_csv(os.path.join(folder_out, 'provider.csv'), index=False)
  dataset_df.drop_duplicates().reset_index(drop=True).to_csv(os.path.join(folder_out, 'dataset.csv'), index=False)
  tag_df.drop_duplicates().reset_index(drop=True).to_csv(os.path.join(folder_out, 'tag.csv'), index=False)
  level1_df.drop_duplicates().reset_index(drop=True).to_csv(os.path.join(folder_out, 'level1.csv'), index=False)
  category_df.drop_duplicates().reset_index(drop=True).to_csv(os.path.join(folder_out, 'category.csv'), index=False)
  provider_dataset_df.drop_duplicates().reset_index(drop=True).to_csv(os.path.join(folder_out, 'provider_dataset.csv'), index=False)
  dataset_tag_df.drop_duplicates().reset_index(drop=True).to_csv(os.path.join(folder_out, 'dataset_tag.csv'), index=False)
  dataset_category_df.drop_duplicates().reset_index(drop=True).to_csv(os.path.join(folder_out, 'dataset_category.csv'), index=False)
  provider_category_df.drop_duplicates().reset_index(drop=True).to_csv(os.path.join(folder_out, 'provider_category.csv'), index=False)
  dataset_level1_df.drop_duplicates().reset_index(drop=True).to_csv(os.path.join(folder_out, 'dataset_level1.csv'), index=False)

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='Turn the md files into csv files for bulk import in neo4j')
  parser.add_argument('--in_fold', type=str, help='Input folder')
  parser.add_argument('--out_fold', type=str, help='Output folder')
  args = parser.parse_args()
  main(args.in_fold , args.out_fold)
