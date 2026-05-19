from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

# GEMINI API KEY
API_KEY = "YAHAN_APNI_GEMINI_API_KEY_DALO"

@app.route("/")
def home():
    return "Gemini Backend Running"

@app.route("/chat", methods=["POST"])
def chat():

    try:
        data = request.get_json()

        user_message = data.get("message", "")

        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"

        payload = {
            "contents": [
                {
                    "parts": [
                        {
                            "text": user_message
                        }
                    ]
                }
            ]
        }

        response = requests.post(url, json=payload)

        result = response.json()

        print(result)

        # SAFE RESPONSE
        if "candidates" in result:

            reply = result["candidates"][0]["content"]["parts"][0]["text"]

        else:

            reply = "Gemini API Error"

        return jsonify({
            "reply": reply
        })

    except Exception as e:

        return jsonify({
            "reply": f"Error: {str(e)}"
        })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
