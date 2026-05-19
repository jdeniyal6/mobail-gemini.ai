from flask import Flask, send_file

app = Flask(__name__)

@app.route("/")
def home():
    return send_file("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    return {
        "reply": "Hello 👋 Gemini Mobile AI Backend Working!"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
