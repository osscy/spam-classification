import text_process_functions as tpf
from joblib import load

def predictNAIVE(text, stemlem):
    tokens = tpf.tokenText(text)
    removed_stopwords = tpf.removeStopwords(tokens)
    
    if stemlem == "stem":
        stem = tpf.stemlem(removed_stopwords,"stemming")
        final_tokens = stem
        return final_tokens
    
    elif stemlem == "lem":
        lem = tpf.stemlem(removed_stopwords,"lemmatization")
        final_tokens = lem
        return final_tokens
    
    #model = load("svm_model_spam.joblib")
text = "hej jag heter oscar"

final = predictNAIVE(text,"stem")
print(final)