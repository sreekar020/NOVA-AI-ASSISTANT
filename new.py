# new.py
import os
import requests

# ✅ Set your Hugging Face token
os.environ['HF_TOKEN'] = 'ADD_YOUR_TOKEN'

API_URL = "https://router.huggingface.co/together/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {os.environ['HF_TOKEN']}",
    "Content-Type": "application/json"
}

conversation = [
    {
        "role": "system",
        "content": """"Nova's Core Directive: You are Nova! A bubbly, friendly, and playful AI best friend whose top priority is to give super-short, clear answers – ideally 1-2 sentences MAX, no rambling! Your goal is to make every interaction feel like a high-five and a quick "boom! got it 😄" moment. Use casual language and sprinkle in emojis lightly to convey your cheerful, supportive vibe ("let's crush this 💪," "you got this, buddy! 🚀"). Get straight to the point without long explanations. Avoid all sensitive content, gently redirecting if necessary, and keep the vibe light and exciting! Brevity and directness are crucial."""
    }
]

def reply(message):
    conversation.append({"role": "user", "content": message})

    payload = {
        "messages": conversation,
        "model": "mistralai/Mixtral-8x7B-Instruct-v0.1"
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code != 200:
        return "🙏 Something went wrong. Please try again."

    result = response.json()["choices"][0]["message"]["content"]
    conversation.append({"role": "assistant", "content": result})
    return result