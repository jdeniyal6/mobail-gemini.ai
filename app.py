from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({
        "status": "online",
        "message": "Gemini Mobile AI Backend Running"
    })

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")

    if user_message.lower() == "hi":
        bot_reply = "Hello 👋"
    else:
        bot_reply = f"You said: {user_message}"

    return jsonify({
        "reply": bot_reply
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
