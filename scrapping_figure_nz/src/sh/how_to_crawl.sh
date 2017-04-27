scrapy runspider ../py/crawl_for_neo4j_import.py -o ../../resources/scrapy_out/figure_nz_for_neo4j.csv -a i_max=84 &> ../../logs/out_scrapy_neo4j.log
scrapy runspider ../py/crawl_for_datasets_urls.py -o ../../resources/scrapy_out/figure_nz_ds_urls.csv -a i_max=84 &> ../../logs/out_scrapy_ds_urls.log
