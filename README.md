# CharacterBasedConvNet
Implementation of Character based Convolution Network inspired from the paper "Character-level Convolutional Networks for Text Classification" written using PyTorch.

Link to the paper => https://arxiv.org/abs/1509.01626

List of the datasets to be used:
1) AG’s News => ag_news_csv
2) Sogou News => sogou_news_csv
3) DBPedia => dbpedia_csv
4) Yelp Review Polarity => yelp_review_polarity_csv

Version 1, Updated 09/09/2015

ORIGIN

The Yelp reviews dataset consists of reviews from Yelp. It is extracted from the Yelp Dataset Challenge 2015 data. For more information, please refer to http://www.yelp.com/dataset_challenge

The Yelp reviews polarity dataset is constructed by Xiang Zhang (xiang.zhang@nyu.edu) from the above dataset. It is first used as a text classification benchmark in the following paper: Xiang Zhang, Junbo Zhao, Yann LeCun. Character-level Convolutional Networks for Text Classification. Advances in Neural Information Processing Systems 28 (NIPS 2015).


DESCRIPTION

The Yelp reviews polarity dataset is constructed by considering stars 1 and 2 negative, and 3 and 4 positive. For each polarity 280,000 training samples and 19,000 testing samples are take randomly. In total there are 560,000 trainig samples and 38,000 testing samples. Negative polarity is class 1, and positive class 2.

The files train.csv and test.csv contain all the training samples as comma-sparated values. There are 2 columns in them, corresponding to class index (1 and 2) and review text. The review texts are escaped using double quotes ("), and any internal double quote is escaped by 2 double quotes (""). New lines are escaped by a backslash followed with an "n" character, that is "\n".

5) Yelp Review Full => yelp_review_full_csv
6) Amazon Review Polarity => amazon_review_polarity_csv
8) Amazon Review Full => amazon_review_full_csv
9) Yahoo! Answers => yahoo_answers_csv
