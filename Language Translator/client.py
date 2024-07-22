import requests
import streamlit as st
import json

def get_groq_response(language,input_text):
    json_body = {
        "inputs": [
            {
                "language": language,
                "text": input_text
            }
        ],    
        "config": {},
        "kwargs": {}
    }

    response=requests.post("http://127.0.0.1:8000/chain/batch",json=json_body)



    return response.json()['output'][0]

## Streamlit app
st.title("LLM Application Using LCEL: Translator")
language=st.text_input("Enter the language you want to translate")
input_text=st.text_input("Enter the text you want to translate")

if input_text:
    st.write(get_groq_response(language,input_text))