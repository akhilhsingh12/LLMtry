import streamlit as st
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

load_dotenv()

st.title("Chat with Mixtral AI")

@st.cache
def generate_chat_response(prompt):
    client = InferenceClient("mistralai/Mixtral-8x7B-Instruct-v0.1")
    chat_completion = client.chat_completion(
        messages=[{"role": "user", "content": prompt}],
        max_tokens=100
    )
    return chat_completion.choices[0].message.content

prompt = st.text_input("Enter your message")
if prompt:
    response = generate_chat_response(prompt)
    st.text_area("Response", response)
