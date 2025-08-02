from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend-backend communication

API_KEY = "AIzaSyD_y7b-knG9NGvXepm3Kp8NerUuquOflW0"  # <- Replace with your valid key
URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"

@app.route("/generate", methods=["POST"])
def generate_code():
    try:
        data = request.json
        user_prompt = data.get("prompt")
        print("Received Prompt:", user_prompt)

        if not user_prompt:
            return jsonify({"error": "No prompt provided"}), 400

        payload = {
            "contents": [
                {"parts": [{"text": user_prompt}]}
            ]
        }

        response = requests.post(URL, json=payload)
        print("Gemini API Status Code:", response.status_code)

        result = response.json()
        print("Gemini API Response:", result)

        # Safely extract text
        if "candidates" in result and result["candidates"]:
            generated_text = result["candidates"][0]["content"]["parts"][0]["text"]
            return jsonify({"generated_code": generated_text})
        else:
            return jsonify({"error": "No candidates found in response"}), 500

    except requests.exceptions.RequestException as e:
        print("Request Exception:", str(e))
        return jsonify({"error": f"Request failed: {str(e)}"}), 500

    except Exception as e:
        print("General Exception:", str(e))
        return jsonify({"error": f"Something went wrong: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
