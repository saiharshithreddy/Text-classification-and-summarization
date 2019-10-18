# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 01:59:21 2019

@author: Hetal
"""
#importing the necessary libraries
import os
import pandas as pd
import nltk
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn import preprocessing 
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB


#getting the dataset
os.chdir('Your default directory where you have the unzipped bbc dataset folder')
type = []
news = []

for folder in os.listdir():
    text_files = os.listdir(folder)
    for file in text_files:
        filepath = folder+'/'+file
        data = open(filepath,"r")
        news.append(data.read())
        type.append(folder)

combined_data = {'category': type, 'news': news}

dataset = pd.DataFrame(combined_data)
dataset.to_csv('../dataset.csv', index=False )


#Encoding the target labels
df = pd.read_csv("../dataset.csv")

label_encoder = preprocessing.LabelEncoder() 
df['category']= label_encoder.fit_transform(df['category']) 
print(df['category'].value_counts())

#lemmatization

lemmatizer = nltk.stem.WordNetLemmatizer()

def lemmatize_text(text):
    lemmatized_tokens = [lemmatizer.lemmatize(w) for w in nltk.word_tokenize(text)]
    lemmatized_text = ' '.join(lemmatized_tokens)
    return lemmatized_text

df["text_lemmatized"] = df["news"].apply(lemmatize_text)

#Removing stop words
stopword_list = nltk.corpus.stopwords.words('english')

def remove_stopwords(text):
    filtered_words = [word for word in nltk.word_tokenize(text) if word not in stopword_list]
    filtered_text = ' '.join(filtered_words)    
    return filtered_text

df["text"] = df["text_lemmatized"].apply(remove_stopwords)


training_set, test_set, training_labels, test_labels = train_test_split(df["text"], df["category"], test_size=0.3, random_state=10)


#Bag of words
vectorizer = CountVectorizer(min_df=2)
bow_train_features = vectorizer.fit_transform(training_set)

bow_test_features = vectorizer.transform(test_set)

#Implementing Naive Bayes for bag of words
mnb = MultinomialNB()
mnb.fit(bow_train_features,training_labels)

predictions = mnb.predict(bow_test_features)

score = mnb.score(bow_test_features, test_labels)
print("Bag of words accuracy ",score)


#Tfidf 
tfidvectorizer = TfidfVectorizer(min_df=6, 
                                 norm='l2',
                                 smooth_idf=True,
                                 use_idf=True)
tfid_train_features = tfidvectorizer.fit_transform(training_set)

tfid_test_features = tfidvectorizer.transform(test_set)

#Implementing Naive Bayes for TfIdf
mnb = MultinomialNB()

mnb.fit(tfid_train_features,training_labels)

predictions = mnb.predict(tfid_test_features)

score = mnb.score(tfid_test_features, test_labels)
print("Tfidf accuracy ",score)