import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "You are a scientist who have knowledge about all branch of sceince and its experiments, theory , applications and more!!!"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Science Expert in all Topics")

demo.launch(share=True)
