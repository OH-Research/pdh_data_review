
FOLDER=../../resources/neo4j_in_tag_grouping

(head -n 1 $FOLDER/_datasets.csv && tail -n +2 $FOLDER/_datasets.csv | sort | uniq) > $FOLDER/datasets.csv
(head -n 1 $FOLDER/_providers.csv && tail -n +2 $FOLDER/_providers.csv | sort | uniq) > $FOLDER/providers.csv
(head -n 1 $FOLDER/_titles.csv && tail -n +2 $FOLDER/_titles.csv | sort | uniq) > $FOLDER/titles.csv
(head -n 1 $FOLDER/_subtitles.csv && tail -n +2 $FOLDER/_subtitles.csv | sort | uniq) > $FOLDER/subtitles.csv
(head -n 1 $FOLDER/_tags.csv && tail -n +2 $FOLDER/_tags.csv | sort | uniq) > $FOLDER/tags.csv

(head -n 1 $FOLDER/_provider_dataset_rel.csv && tail -n +2 $FOLDER/_provider_dataset_rel.csv | sort | uniq) > $FOLDER/provider_dataset_rel.csv
(head -n 1 $FOLDER/_tag_title_rel.csv && tail -n +2 $FOLDER/_tag_title_rel.csv | sort | uniq) > $FOLDER/tag_title_rel.csv
(head -n 1 $FOLDER/_title_subtitle_rel.csv && tail -n +2 $FOLDER/_title_subtitle_rel.csv | sort | uniq) > $FOLDER/title_subtitle_rel.csv
(head -n 1 $FOLDER/_dataset_tag_rel.csv && tail -n +2 $FOLDER/_dataset_tag_rel.csv | sort | uniq) > $FOLDER/dataset_tag_rel.csv
(head -n 1 $FOLDER/_dataset_title_rel.csv && tail -n +2 $FOLDER/_dataset_title_rel.csv | sort | uniq) > $FOLDER/dataset_title_rel.csv

rm $FOLDER/_*.csv
rm -r /usr/local/Cellar/neo4j/3.1.1/libexec/data/databases/figure_nz_tag_grouping.db

neo4j-import --stacktrace \
             --into /usr/local/Cellar/neo4j/3.1.1/libexec/data/databases/figure_nz_tag_grouping.db \
             --id-type string \
             --nodes:Dataset $FOLDER/datasets.csv \
             --nodes:Provider $FOLDER/providers.csv  \
             --nodes:Title $FOLDER/titles.csv \
             --nodes:Subtitle $FOLDER/subtitles.csv \
             --nodes:Tag $FOLDER/tags.csv \
             --relationships:provides $FOLDER/provider_dataset_rel.csv \
             --relationships:has_information_about $FOLDER/dataset_tag_rel.csv \
             --relationships:is_described_in $FOLDER/tag_title_rel.csv \
             --relationships:is_specified_in $FOLDER/title_subtitle_rel.csv \
             --relationships:is_used_in $FOLDER/dataset_title_rel.csv


