from flask import Flask, jsonify, request
import text_process_functions as tpf
from joblib import load


app = Flask(__name__)

@app.route("/naive/<string:stemlem>", methods = ["POST"])
def predictNAIVE(stemlem):
    text = request.data.decode("utf-8")
    final_tokens = []
    tokens = tpf.tokenText(text)
    removed_stopwords = tpf.removeStopwords(tokens)
    
    if stemlem == "stem":
        stem = tpf.stemlem(removed_stopwords,"stemming")
        final_tokens = stem
        print(removed_stopwords)
    
    elif stemlem == "lem":
        lem = tpf.stemlem(removed_stopwords,"lemmatization")
        final_tokens = lem
    
    else:
        return jsonify({"error":"not stemming nor lemmatization"}), 404

    #encode the text ---> use same bag of word as before

    model = load("saved-model\\naive_bayes_model_spam.joblib")

    prediction = model.predict(final_tokens)

    return jsonify(prediction), 404


if __name__=="__main__":
    app.run(debug=True)

 