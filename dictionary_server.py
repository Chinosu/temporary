from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)


# Load dictionary data from JSON file
with open("dictionary.json", "r") as f:
    dictionary = json.load(f)


@app.route("/api/word/<string:word>", methods=["GET"])
def get_word_definition(word):
    word = word.lower()
    matching_words = {k: v for k, v in dictionary.items() if word in k.lower()}

    return jsonify(matching_words[0:50])


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
