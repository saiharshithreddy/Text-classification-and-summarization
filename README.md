# Text-classification-and-summarization

### Text classification:
Classifying the news articles into 4 categories namely Health, Business, Entertainment, Technology using the following ML models:  
1. Logistic regression
2. Support Vector Machine
3. Naive Bayes 
4. Random forest
5. K-NN


### Text summarization:
Summarize the news articles using Extractive text summarization ( selecting top sentences from the article)

#### Models for extractive summarization:
1. Text rank algorithm (variation of page rank)
2. K-means clustering
3. Latent semantic analysis


### Data:
Scrapped news articles from urls provided by UCI Machine Learning repository [link](http://archive.ics.uci.edu/ml/datasets/News+Aggregator)  
For scrapping the news articles, ```Newspaper3k``` [library](https://newspaper.readthedocs.io/en/latest/) built in Python was used. The library contains ```nlp()``` method using which *keywords* and *summary* of the news article can be extracted.   
Article's content and summary have been scrapped to create the data for the project. [Code](https://github.com/saiharshithreddy/Text-classification-and-summarization/blob/master/Data%20collection/data%20scrapper.ipynb)  

### Installation
The following libraries of Python have to be installed: ```pandas```, ```sklearn```, ```ntlk```, ```newspaper3k```  
Run the following command to install
```pip install -r requirements.txt```

### Data preprocessing
Raw text has unwanted characters (\n,\t,$ etc) and contains stop words (a, an, the) which has to removed before generating the vector representation. The following text preprocessing techniques have been used:  
1. Converting to lower case
2. Removal of stop words
3. Tokenize
4. Removing contractions (does'nt -> does not)
5. Stemming/Lemmatization


### Results

#### Text classification
| S.no | Model | Accuracy |
|------|-------|----------|
|1. | Logistic regression | |
|2. | SVM | |
|3. | Naive Bayes | |
|4. | Random forest | |
|5. | K-NN | |


#### Text summarization
| S.no | Model | Accuracy |
|------|-------|----------|
|1. | Text rank | |
|2. | K-means clustering| |
|3. | Latent semantic analysis | |

