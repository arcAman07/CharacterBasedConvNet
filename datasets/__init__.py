import tarfile
import wget
import pandas as pd
import numpy as np
import config
wget.download(config.ag_news_csv)
wget.download(config.amazon_review_full_csv)
wget.download(config.amazon_review_polarity_csv)
wget.download(config.dbpedia_csv)
wget.download(config.yahoo_answers_csv)
wget.download(config.sogou_news_csv)
wget.download(config.yelp_review_full_csv)
wget.download(config.yelp_review_polarity_csv)

# tf  = tarfile.open( "/content/dbpedia_csv.tgz")
# tf.extractall()
# %%capture
# %cd dbpedia_csv/
