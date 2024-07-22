# Importing required libraries
import os
from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langserve import add_routes
from langchain_groq import ChatGroq
# To use OpenAI model
# from langchain_openai import ChatOpenAI 

# LLM model 
groq_api_key = "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"
model = ChatGroq(model="Gemma2-9b-It",groq_api_key=groq_api_key)

# Langsmith Tracking
os.environ["LANGCHAIN_API_KEY"]="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"
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]="Language_Translator"

# Creating Prompt Template
system_template = "Translate the following into {language}:"
prompt_template = ChatPromptTemplate.from_messages([
    ("system",system_template),
    ("user",'{text}')
])

#Creating output parser
output_parser = StrOutputParser()

# Creating chain using LCEL : Langchain Expression Language
chain = prompt_template|model|output_parser

# App defination
app = FastAPI(title="Langchain Server",
              version = "1.0",
              description = "A simple API server using Langchain runnable interfaces")

# Adding chain routes
add_routes(
    app,
    chain,
    path="/chain"
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host = "127.0.0.1", port = 8000)






