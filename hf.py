import os
from huggingface_hub import InferenceClient
from huggingface_hub import InferenceApi
from dotenv import load_dotenv

load_dotenv()

client = InferenceClient("mistralai/Mixtral-8x7B-Instruct-v0.1")
#response=client.text_generation("Tell me a joke")
chat_completion=client.chat_completion(

    messages=[
        {
            "role": "user",
            "content": "Tell me a joke about marriage",
        }
    ], max_tokens=100)

# hf_client = InferenceApi(repo_id="gpt-2", token=os.environ['HF_KEY']) 

#generated_text = client.text_generation(prompt="Write a code for snake game")
print(chat_completion.choices[0].message.content)

# response = hf_client(text="The definition of machine learning inference is")

# print(response)

# 'model': "HuggingFaceH4/zephyr-7b-beta"