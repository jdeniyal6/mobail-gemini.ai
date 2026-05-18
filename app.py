from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/chat", methods=["POST"])
def chat():

    data = request.json

    msg = data.get("message","").lower()

    if "hello" in msg:
        reply = "Hello 👋"

    elif "your name" in msg:
        reply = "I am Gemini Mobile AI"

    elif "how are you" in msg:
        reply = "I am fine 🚀"

    else:
        reply = "You said: " + msg

    return jsonify({
        "reply": reply
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
