import os
import openai
import gradio as gr
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

def CustomChatGPT(user_input):
    messages = [{"role": "system", "content": "You are a financial experts that specializes in real estate investment and negotiation"}]
    messages.append({"role": "user", "content": user_input})
    
    response = openai.ChatCompletion.create(
        api_key=api_key,
        model="gpt-3.5-turbo",
        messages=messages
    )
    
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    return ChatGPT_reply

demo = gr.Interface(fn=CustomChatGPT, inputs="text", outputs="text", title="Real Estate Pro")
demo.launch(share=True)
