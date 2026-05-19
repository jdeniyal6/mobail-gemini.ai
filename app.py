from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

OPENROUTER_API_KEY = "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"

@app.route("/")
def home():
    return "OpenRouter Backend Running"

@app.route("/chat", methods=["POST"])
def chat():

    try:

        data = request.get_json()
        user_message = data.get("message", "")

        response = requests.post(

            url="https://openrouter.ai/api/v1/chat/completions",

            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json"
            },

            json={
                "model": "deepseek/deepseek-chat:free",

                "messages": [
                    {
                        "role": "user",
                        "content": user_message
                    }
                ]
            }
        )

        result = response.json()

        print(result)

        reply = result["choices"][0]["message"]["content"]

        return jsonify({
            "reply": reply
        })

    except Exception as e:

        return jsonify({
            "reply": f"Error: {str(e)}"
        })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
