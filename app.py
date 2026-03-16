from flask import Flask, render_template, jsonify
from speech import recognize_speech

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/listen")
def listen():
    text = recognize_speech()
    return jsonify({"caption": text})

if __name__ == "__main__":
    app.run(debug=True)