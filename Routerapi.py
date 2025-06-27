import requests

OPENROUTER_API_KEY = "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"  # Replace with your actual key
MODEL = "deepseek/deepseek-r1-0528"  # Or another model from OpenRouter

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
