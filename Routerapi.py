import requests

OPENROUTER_API_KEY = "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"  # Replace with your actual key
MODEL = "mistralai/mixtral-8x7b"  # Or another model from OpenRouter

def generate_ad(content):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "You are a creative AI that generates compelling marketing ads based on website content."},
            {"role": "user", "content": f"Create a short marketing ad copy based on the following website content:\n\n{content}"}
        ]
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", json=data, headers=headers)
    
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return f"❌ Error: {response.status_code} - {response.text}"
