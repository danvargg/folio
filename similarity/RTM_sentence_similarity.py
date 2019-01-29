# coding: utf-8
#https://sites.temple.edu/tudsc/2017/03/30/measuring-similarity-between-texts-in-python/

import nltk, string, numpy

#nltk.download('punkt') # first-time use only

stemmer = nltk.stem.porter.PorterStemmer()

def StemTokens(tokens):
  return [stemmer.stem(token) for token in tokens]

remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

def StemNormalize(text):
  return StemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

# Lemmatization

#nltk.download('wordnet') # first-time use only

lemmer = nltk.stem.WordNetLemmatizer()

def LemTokens(tokens):
  return [lemmer.lemmatize(token) for token in tokens]

remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

def LemNormalize(text):
  return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

# Text to vectors of term frequency

from sklearn.feature_extraction.text import CountVectorizer

LemVectorizer = CountVectorizer(tokenizer=LemNormalize, stop_words='english')
LemVectorizer.fit_transform(documents)

LemVectorizer.vocabulary_

tf_matrix = LemVectorizer.transform(documents).toarray()
tf_matrix

# Get IDF

from sklearn.feature_extraction.text import TfidfTransformer

tfidfTran = TfidfTransformer(norm = "l2")
tfidfTran.fit(tf_matrix)

tfidfTran.idf_


import math

def idf(n,df):
    result = math.log((n+1.0)/(df+1.0)) + 1
    return result

print("The idf for terms that appear in one document: " + str(idf(4,1)))
print("The idf for terms that appear in two documents: " + str(idf(4,2)))

tfidf_matrix = tfidfTran.transform(tf_matrix)
tfidf_matrix.toarray()

# SKLearn implementation
 
# Scikit-learn actually has another function TfidfVectorizer that combines the work of CountVectorizer and TfidfTransformer, which makes the process more efficient.

import pandas as pd
data = pd.read_excel('RTM_SDIVM_27_Master_Data_Change_Management v16_R5.xlsx', sheet_name = 'L1 Requirements')
data = data[data.Status != 'Cancelled']
data['text'] = data['Description \n(Stakeholder: I want to <goal or need>)'].astype(str) + data['So that <Justification> ']
req = data[['Requirement ID', 'text']]
req = req.dropna(how = 'all')

req.shape
req.isnull().any()

reqs = req['text'].values

from sklearn.feature_extraction.text import TfidfVectorizer

TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')

def cos_similarity(textlist):
    tfidf = TfidfVec.fit_transform(textlist)
    return (tfidf * tfidf.T).toarray()

similarity = pd.DataFrame(cos_similarity(reqs))

similarity.isnull().any()

similarity['Requirement ID'] = req['Requirement ID']

#similarity.columns = similarity['Requirement ID']

similarity
