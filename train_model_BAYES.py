from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.naive_bayes import MultinomialNB

from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_validate

import pandas as pd

import joblib

data = pd.read_csv("processed_data.csv")

use_data = data["stem_words"]
label_data = data["type"] 

#create hashingvectorizer
vector = TfidfVectorizer()
data = vector.fit_transform(use_data)

x = data
y = label_data

#split data to train and text
x_train, x_test, y_tain, y_text = train_test_split(x, y, test_size=0.33, random_state= 42)

#create model
naive_bayer = MultinomialNB()

#cross validate and grid search to find best model
parameters = {
    "alpha": [0.0001, 0.001, 0.1, 1, 10, 100]
}

#create gird
grid = GridSearchCV(naive_bayer, parameters, cv = 5, scoring = "accuracy")

#run model with all sets of parameters
grid.fit(x_train, y_train)

#get model and parameters
best_model = grid.best_estimator_

#make predictions with best model
y_pred = best_model.predict(x_test)

report = classification_report(y_test, y_pred)

print(grid.best_params_)
print(grid.best_score_)
print(report)

#save model
joblib.dump(best_model, "saved-model\\naive_bayes_model_spam.joblib")


