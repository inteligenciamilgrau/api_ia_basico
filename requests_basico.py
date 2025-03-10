import requests
from dotenv import load_dotenv
import os

load_dotenv()
openai_token = os.getenv("OPENAI_API_KEY")

headers = {
    "Authorization": f"Bearer {openai_token}",
    "Content-Type": "application/json"
}

data = {
    "model": "gpt-4o-mini",
    "messages": [
        {
            "role": "user",
            "content": "Qual a capital do Brasil?"
        }
    ],
    "max_tokens": 500,
    "stream": False
}

response = requests.post(
    "https://api.openai.com/v1/chat/completions",
    headers=headers,
    json=data
)

if response.status_code == 200:
    print("Resposta Completa:")
    print(response.json())
    print("\nResposta (apenas o texto):")
    print(response.json()["choices"][0]["message"]["content"])
else:
    print(f"Error: {response.status_code}")
    print(response.text)