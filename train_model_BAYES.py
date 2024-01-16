from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd

data = pd.read_csv("processed_data.csv")

use_data = data["stem_words"]
label_data = data["type"] 

#create hashingvectorizer
hash_vector = HashingVectorizer()
data = hash_vector.fit_transform(use_data)

x = data
y = label_data

#split data to train and text
x_train, x_test, y_tain, y_text = train_test_split(x, y, test_size=0.33, random_state= 42)

#use pipeline 

