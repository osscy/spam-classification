import pandas as pd

#load data
df_large = pd.read_csv("enron_spam_data.csv")

#drop message ID, subject and date --> columns that is not needed
df_large.drop(["Message ID","Subject","Date"], axis = 1, inplace = True)

#remove null values
df_large[df_large["text"].isnull() == True].index
df_large.drop(df_large[df_large["text"].isnull() == True].index, inplace = True)

#convert spam = 1 and ham = 0
def changeToNum(typ):
  if typ == "spam":
    return 1
  else:
    return 0

df_large["type"] = df_large["type"].apply(changeToNum)

#change to int
df_large["type"] = df_large["type"].astype(int)


#drop duplicates
df_large.drop_duplicates(subset = "text",inplace = True)


