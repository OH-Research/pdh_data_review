
FOLDER=out

rm -r /usr/local/Cellar/neo4j/3.1.1/libexec/data/databases/graph.db

neo4j-import --stacktrace \
             --multiline-fields=true \
             --into /usr/local/Cellar/neo4j/3.1.1/libexec/data/databases/graph.db \
             --id-type string \
             --nodes:Dataset $FOLDER/dataset.csv \
             --nodes:Provider $FOLDER/provider.csv  \
             --nodes:Tag $FOLDER/tag.csv \
             --nodes:Level1 $FOLDER/level1.csv \
             --nodes:Category $FOLDER/category.csv \
             --relationships:provides $FOLDER/provider_dataset.csv \
             --relationships:contains_information_about $FOLDER/dataset_tag.csv \
             --relationships:fall_into $FOLDER/dataset_category.csv \
             --relationships:provides_dataset_falling_into $FOLDER/provider_category.csv \
             --relationships:is_detailed_in $FOLDER/dataset_level1.csv


