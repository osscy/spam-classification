import nltk
from nltk.corpus import stopwords
import pandas as pd
        
#fromt words we want must we remove ex links, or special tokens taht can be in a words, that did not get removed before. 
#ex can find words like: 1000%! or go:https, or words with ! in them. 
#thus if a word contain these, will we remove the word

def createStopwordFile():
    #get stopwords and create a list --> save as txt file
    #download if not done
    #nltk.download("stopwords")

    stopw = stopwords.words("english")
    #extra tokens, that i want to remove, no meaning for text
    list_extra = ["http","|",'"',";","/","?",",",".","-","_","!","@","#","£","¤","$","%","€","&","{","(","[",")","]","=","}","+",'\'',"`","*","'","^",":","1","2","3","4","5","6","7","8","9","0"]

    #write to file
    with open("C:\\Users\\osci1\\OneDrive\\JupyterNotebook\\stopwords.txt", "w", encoding="utf-8") as file:
        for word in stopw:
            file.write(word + "\n")

        #add extra
        for char in list_extra:
            file.write(char + "\n")

def getStopWords():
    #open stopword file and get a list of all word
    words_stop = []
    with open("C:\\Users\\osci1\\OneDrive\\JupyterNotebook\\stopwords.txt", "r") as rfile:
        words = rfile.read()
        words_stop = words.split()
    return words_stop

def tokenText(int_str):
    str_split = int_str.split()
    str_split = [i.lower() for i in str_split]
    return str_split

def removeStopWords(stop, extra_list, words):
    filtered_words = []
    for word in words:
        if word not in stop:
            filtered_words.append(word)
    
    #remove extra tokens if they are in the word
    index = 0
    for fw in filtered_words:
        #will replace links, they usually has htts
        #must see if this affects the result or not
        
        if "http" in fw:
            fw = fw.replace(fw,"")
            filtered_words[index] = fw
        
        #check for extra tokens in each word
        #if word has token --> remove token from word, this is example hello% --> hello
        #must use extra list, otherwise will it remove alost every character
        for char in fw:
            if char in extra_list:
                fw = fw.replace(char, "")
                filtered_words[index] = fw
        
        #remove empty value in string if we got any
        while("" in filtered_words):
            filtered_words.remove("")
        
        index  += 1
    
    return filtered_words


def createBagWord(filtered_text, bag):
    """add words to the bag of words"""

    #if a words it not in bag_of_word add it and set the value to zero
    for tok in filtered_text:
        while tok not in list(bag.keys()):
            bag[tok] = 0

    #create a txt file 
    with open("C:\\Users\\osci1\\OneDrive\\JupyterNotebook\\bagofword.txt", "w", encoding="utf-8") as file:
        for word in list(bag.keys()):
            file.write(word.encode("utf-8") + "\n")  


def createDicOfBagWord():
    """create a dictionary of all words in the bag of words"""

    bag_words = []
    with open("C:\\Users\\osci1\\OneDrive\\JupyterNotebook\\bagofword.txt", "r") as bagfile:
        words = bagfile.read()
        bag_words = words.split()
    
    text_dic = {}
    for bw in bag_words:
        while bw not in list(text_dic.keys()):
            text_dic[bw] = 0          
    
    return text_dic
    
def countWords(bag_of_word_dic, filtered_text):
    """Count the numbe of words in each filtered text and add it to the dictionary"""
    for tok in filtered_text:
        if tok in list(bag_of_word_dic.keys()):
            bag_of_word_dic[tok] = bag_of_word_dic[tok] + 1   
    
    return bag_of_word_dic

def createVector(dic_words):
    vector = [num for num in list(dic_words.values())]
    return vector



df = pd.read_csv("C:\\Users\\osci1\\OneDrive\\JupyterNotebook\\Phishing_Email.csv")
phis = df[df["Email Type"] == "Phishing Email"]


list_string = [phis["Email Text"].iloc[5778]]
print(list_string)

"""
#create stopWords
createStopwordFile()
stop_words = getStopWords()

#first create the bag of word
word_bag = {}
for str3 in list_string:
    split_string = tokenText(str3)

    list_extra = ["Â","|",'"',";","/","?",",",".","-","_","!","@","#","£","¤","$","%","€","&","{","(","[",")","]","=","}","+",'\'',"`","*","'","^",":","1","2","3","4","5","6","7","8","9","0"]

    filtered_words = removeStopWords(stop_words,list_extra,split_string)
    createBagWord(filtered_words, word_bag)


for str3 in list_string:
    split_string = tokenText(str3)

    list_extra = ["|",'"',";","/","?",",",".","-","_","!","@","#","£","¤","$","%","€","&","{","(","[",")","]","=","}","+",'\'',"`","*","'","^",":","1","2","3","4","5","6","7","8","9","0"]

    filtered_words = removeStopWords(stop_words,list_extra,split_string)

    word_dic = createDicOfBagWord()

    counted = countWords(word_dic, filtered_words)
    
    vector = createVector(counted)
"""