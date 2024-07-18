from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# Load dictionary data from JSON file
with open("dictionary.json", "r") as f:
    dictionary = json.load(f)


@app.route("/api/word/<string:word>", methods=["GET"])
def get_word_definition(word):
    word = word.lower()
    matching_words = {k: v for k, v in dictionary.items() if word in k.lower()}
    return jsonify(matching_words)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
