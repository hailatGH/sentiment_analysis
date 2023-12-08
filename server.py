import os, random
from flask import Flask, request, jsonify
from transformers import pipeline

sent_pipeline = pipeline("sentiment-analysis")

app = Flask(__name__)

@app.route("/analyse", methods=["POST"])
def analyse():
    data = request.get_json()
    text = data['text']
    res = sent_pipeline(text)
    return jsonify(res)


if __name__ == "__main__":
    app.run(debug=False)













