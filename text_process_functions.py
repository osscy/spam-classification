import pandas as pd

from nltk.corpus import stopwords
import nltk
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import *

nltk.download("punkt")
nltk.download("english")
nltk.download("stopwords")
nltk.download("wordnet")

#used for token text, use tokenizer from nltk
def tokenText(text):
  tokens = word_tokenize(text)
  return tokens

#remove stopwords and return new token list
def removeStopwords(tokens):
  stopw = stopwords.words("english")

  extra_list = ["|",'"',";","/","?",",",".","-","_","!","@","#","£","¤","$","%","€",
                  "&","{","(","[",")","]","=","}","+",'\'',"`","*","'","^",":","``","´´","<",">"]
  stopw.extend(extra_list)

  stoplist = []
  for token in tokens:
    if token not in stopw:
      stoplist.append(token)

  return stoplist

#get the stem or lem for each word
def stemlem(tokens, typ):
    """return a list of stemming or lemmatization of the tokens
    """
    if typ == "stemming":
        stemmer = PorterStemmer()
        stemwords = [stemmer.stem(tok) for tok in tokens]
        return stemwords

    if typ == "lemmatization":
        lemmitazer = WordNetLemmatizer()
        lemwords = [lemmitazer.lemmatize(tok) for tok in tokens]
        return lemwords

