import requests

API_KEY = "ADD_YOUR_API_KEY"
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"

data = {
    "contents": [
        {"parts": [{"text": "what is ai"}]}
    ]
}

response = requests.post(url, json=data)
result = response.json()

# Extracting the generated text
generated_text = result["candidates"][0]["content"]["parts"][0]["text"]

# Print cleaned output
print("\n📝 Generated Code:\n")
print(generated_text)
