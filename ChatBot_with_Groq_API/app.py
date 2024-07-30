import streamlit as st
# import openai
import langchain
# from langchain_openai import ChatOpenAI
# from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq

import os
from dotenv import load_dotenv
load_dotenv() 


#langsmith Tracking
os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_KEY")
os.environ['LANGCHAIN_TRACING_V2'] = "true"
os.environ['LANGCHAIN_PROJECT'] = "Q&A Chat-Bot with OpenAI"

# Prompt templates
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant, Please respond to the user queries"),
        ("user","Question:{question}")
    ]
)

def generate_response(question,api_key,llm,temperature,max_tokens):
    #openai.api_key=api_key
    #llm = ChatOpenAI(model=llm)
    #llm = Ollama(model=llm)
    llm = ChatGroq(groq_api_key=api_key, model_name=llm)
    outputparser=StrOutputParser()
    chain=prompt|llm|outputparser
    answer = chain.invoke({"question":question})
    return answer

# Title of the app
st.title("ChatBot with Groq API")

# Side bar for settings
st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Enter your Groq API Key:",type="password")

# Drop down to select different models
llm = st.sidebar.selectbox("Select the model",['Gemma-7b-It','Gemma2-9b-It','Mixtral-8x7b-32768'])

# Adjust response parameter
temperature = st.sidebar.slider("Temperature",min_value=0.0,max_value=1.0,value=0.7)
max_tokens = st.sidebar.slider("Max tokens",min_value=50,max_value=300,value=150)

# main interface for user input
st.write("Go ahead and ask any question")
user_input = st.text_input("You:")

if user_input:
    response = generate_response(user_input,api_key=api_key,llm=llm,temperature=temperature,max_tokens=max_tokens)
    st.write(response)
else:
    st.write("Please ask the question")





