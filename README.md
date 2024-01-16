# spam-classification

## Description and goal

The main goal of this project is to build a text classifier that can classify spam and non-spam emails by the content in the email.

***Question: Can a classification model predict spam mails from a set of mails by analyzing the text content of mails***

This is done by using the Enron Spam Dataset dataset from: https://github.com/MWiechmann/enron_spam_data/blob/master/README.md

The dataset is originally collected by V. Metsis, I. Androutsopoulos and G. Paliouras in one of their publication: "Spam Filtering with Naive Bayes - Which Naive Bayes?"

From github can the csv file be obtained where there are 4 columns: Date, Subject, message and spam/ham. I will only use the message and spam/ham column because these do contain only the message as pure text and if the message is a spam or ham.

### Outline
First EDA will be done to investigate and understand the texts from the dataset.

To be able to process it in ML algorithm must the text be converted to vectors, this is done by using Countvectorizer library and TfidfVectorizer library from scikit learn with bag of words. Countvectorize will represent the unique words in bag of words as counts and TF-IDF will calculate a score by multiplying the term frequency by the inverse document frequency. In both cases will a matrix be produced where each row is an text document and each column is an unique word.

ML models that are used are Naive bayes and SVM from scikit learn.

Naive bayes and Support Vector Machine was chosen because according to literature should these two models be great for text classification.
Source: https://www.ceom.ou.edu/media/docs/upload/Pang-Ning_Tan_Michael_Steinbach_Vipin_Kumar_-_Introduction_to_Data_Mining-Pe_NRDK4fi.pdf
https://www.cs.cornell.edu/people/tj/publications/joachims_98a.pdf  

Metrics to evaluate the different models will be done with mainly accuracy, but also precision, recall and fscore. These metrics should be good to use for classification and when the dataset it balanced.
Source: https://www.analyticsvidhya.com/blog/2021/07/metrics-to-evaluate-your-classification-model-to-take-the-right-decisions/