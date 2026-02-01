import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("HF_API_KEY")

url = "https://router.huggingface.co/hf-inference/models/mistralai/Mistral-7B-Instruct-v0.3"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

payload = {
    "model": "mistralai/Mistral-7B-Instruct-v0.3",
    "inputs": "Say hello in one short sentence."
}

print("🚀 Calling HuggingFace API...")

response = requests.post(url, headers=headers, json=payload)

print("Status code:", response.status_code)
print("Response:")
print(response.text)
