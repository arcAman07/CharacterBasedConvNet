import list_datasets
import os
from list_datasets import *
import torchvision
from torchvision.datasets.utils import download_url
import tarfile
import cleaning
from cleaning import *
import encoding
from encoding import *
# Download the dataset
download_url(yelp_review_polarity_csv, '.')

# Extract from archive
with tarfile.open('./yelp_review_polarity_csv.tgz', 'r:gz') as tar:
    tar.extractall(path='./data')
    
# Look into the data directory
data_dir = './data/yelp_review_polarity_csv'
print(os.listdir(data_dir))
print(ag_news_csv)

# Reading the train dataset from the csv file
train_data = pd.read_csv("/content/data/yelp_review_polarity_csv/train.csv")

# Reading the train dataset from the csv file
test_data = pd.read_csv("/content/data/yelp_review_polarity_csv/test.csv")