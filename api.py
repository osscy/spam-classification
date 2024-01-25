from flask import Flask, jsonify
import text_process_functions as tpf
from joblib import load

app = Flask(__name__)

@app.route("/naive/<string:stemlem>/<string:text>", methods = ["GET"])
def predictNAIVE(text, stemlem):
    final_tokens = []
    tokens = tpf.tokenText(text)
    removed_stopwords = tpf.removeStopwords(tokens)
    
    if stemlem == "stem":
        stem = tpf.stemlem(removed_stopwords,"stemming")
        final_tokens = stem
    
    elif stemlem == "lem":
        lem = tpf.stemlem(removed_stopwords,"lemmatization")
        final_tokens = lem
    
    else:
        return jsonify({"error":"not stemming nor lemmatization"}), 404

    model = load("svm_model_spam.joblib")

 