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
                  "&","{","(","[",")","]","=","}","+",'\'',"`","*","'","^",":","``","´´","ect", "hou","enron", "2000", "e", "S", "hpl", "cc", "mmbtu", "00", "000", "ga","<",">"]
  stopw.extend(extra_list)

  stoplist = []
  for token in tokens:
    if token not in stopw:
      stoplist.append(token)

  return stoplist