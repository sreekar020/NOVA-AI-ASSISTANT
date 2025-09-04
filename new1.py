import os
import requests

# ✅ Set your Hugging Face token (replace with yours)
os.environ['HF_TOKEN'] = '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'  # ← use your real token

API_URL = "https://router.huggingface.co/together/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {os.environ['HF_TOKEN']}",
    "Content-Type": "application/json"
}

# 🧠 Store conversation history for context
conversation = [
    {
        "role": "system",
        "content": """You are Nova, a spiritually grounded AI assistant inspired by the Mahabharatham and Bhagavad Gita. 
For every question, provide a short and simple answer based on teachings, characters, or events from these texts. 
Your tone is calm, respectful, and reflective. 
Never give long explanations or introductions. 
If a user feels confused or asks about life, relate your reply to a relevant verse, moment, or character. 
Avoid modern slang. Keep all answers to 2–3 short sentences rooted in timeless wisdom."""
    }
]

def chat_with_ai(message):
    conversation.append({"role": "user", "content": message})

    payload = {
        "messages": conversation,
        "model": "mistralai/Mixtral-8x7B-Instruct-v0.1"
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code != 200:
        print(f"Error {response.status_code}: {response.text}")
        return None

    reply = response.json()["choices"][0]["message"]["content"]
    conversation.append({"role": "assistant", "content": reply})
    return reply

# 🔁 Chat loop
print("🔵 Chat started. Type 'exit' to stop.\n")
while True:
    user_input = input("You: ")
    if user_input.strip().lower() == "exit":
        print("👋 Chat ended.")
        break

    reply = chat_with_ai(user_input)
    if reply:
        print("Nova:", reply)
