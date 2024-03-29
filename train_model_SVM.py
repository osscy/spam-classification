from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn import svm

from sklearn.model_selection import GridSearchCV

import pandas as pd

import joblib

data = pd.read_csv("processed_data.csv")

use_data = data["stem_words"]
label_data = data["type"] 

#create tfidfvectors
vector = TfidfVectorizer()
data = vector.fit_transform(use_data)

x = data
y = label_data

#split data to train and text
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state= 42)

model = svm.SVC()

parameters = {"C": [0.01, 0.1, 1, 5, 10], "kernel": ["linear", "rbf"]}

#create gird
grid = GridSearchCV(model, parameters, cv = 5, scoring = "accuracy")

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
joblib.dump(best_model, "saved-model\\svm_model_spam.joblib")