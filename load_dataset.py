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
import parameters
from parameters import *
from torch.utils.data import Dataset
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
train_data = pd.read_csv("data/yelp_review_polarity_csv/train.csv")

# Reading the train dataset from the csv file
test_data = pd.read_csv("data/yelp_review_polarity_csv/test.csv")

train_dataset =  []

for i in range(0, len(train_data)):
  text = train_data.iloc[i,1]
  if len(list(text)) > 1014:
    text = text[0:1014]
  label = train_data.iloc[i,0]
  sentence_tensor = compute_oneHotEncoding(text)
  train_dataset.append((sentence_tensor,label))

train_dataset = torch.Floattensor(train_dataset)

text, label = train_dataset[0]
print("Label :",label)
print("Encoding: ",text)
print("Shape: ",text.shape)