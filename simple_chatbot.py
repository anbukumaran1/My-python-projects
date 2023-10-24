import requests
import json

api_key = "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"

def chat_with_bot(input_text):
    url = "https://api.openai.com/v1/engines/davinci-codex/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    data = {
        "prompt": input_text,
        "max_tokens": 100,  # Adjust as needed
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()["choices"][0]["text"]


user_input = input("You: ")
while user_input.lower() != "exit":
    bot_response = chat_with_bot(user_input)
    print(f"Chatbot: {bot_response}")
    user_input = input("You: ")