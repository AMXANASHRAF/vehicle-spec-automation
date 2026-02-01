import requests
import json
from pathlib import Path


# -------------------------------------------------
# Project root (VIN Project/)
# -------------------------------------------------
ROOT = Path(__file__).resolve().parents[2]


# -------------------------------------------------
# Load prompt template
# -------------------------------------------------
def load_prompt(filename="spec_extraction_prompt.txt"):
    prompt_path = ROOT / "prompts" / filename

    with open(prompt_path, "r", encoding="utf-8") as f:
        return f.read()


# -------------------------------------------------
# Query HuggingFace (router endpoint)
# -------------------------------------------------
def query_hf(prompt, api_key):

    url = "https://router.huggingface.co/hf-inference"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "mistralai/Mistral-7B-Instruct-v0.3",  # ✅ UPDATED MODEL
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 400,
            "temperature": 0.1,
            "return_full_text": False
        }
    }

    response = requests.post(url, headers=headers, json=payload, timeout=60)

    if response.status_code != 200:
        raise Exception(f"HF API Error: {response.text}")

    return response.json()["generated_text"]


# -------------------------------------------------
# Extract specs
# -------------------------------------------------
def extract_specs(vehicle_text, api_key):

    template = load_prompt()

    prompt = template.replace("{vehicle_text}", vehicle_text)

    raw_output = query_hf(prompt, api_key)

    try:
        return json.loads(raw_output)
    except:
        print("⚠️ Invalid JSON from model:")
        print(raw_output)
        return None
