# Text-classification-and-summarization

#### Text classification:
Classifying the news articles into 4 categories namely Health, Business, Entertainment, Technology using the following ML models:  
1. Logistic regression
2. Support Vector Machine
3. Naive Bayes 
4. Random forest
5. K-NN


#### Text summarization:
Summarize the news articles in two ways: Extractive text summarization ( selecting top sentences from the article) and Abstractive text summarization ( generating a summary).

#### Models for extractive summarization:
1. Text rank algorithm (variation of page rank)
2. K-means clustering
3. Latent semantic analysis

#### Models for abstractive summarization:
1. Seq2Seq with attention

**Data:** Scrapped news articles from urls provided by UCI Machine Learning repository [link](http://archive.ics.uci.edu/ml/datasets/News+Aggregator)  
For scrapping the news articles, ```Newspaper3k``` [library](https://newspaper.readthedocs.io/en/latest/) built in Python was used. The library contains ```nlp()``` method using which *keywords* and *summary* of the news article can be extracted.   
Article's content and summary have been scrapped to create the data for the project. [Code](https://github.com/saiharshithreddy/Text-classification-and-summarization/blob/master/Data%20collection/data%20scrapper.ipynb)  
