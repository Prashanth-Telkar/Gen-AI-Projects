# Language Translator using Gemma2-9b-It from Groq
This project implements a generative AI application for language translation, utilizing FastAPI for backend endpoints and Streamlit for the frontend UI. The application allows users to specify the target language and input text for translation.

# Frameworks and Technologies:
FastAPI: Python web framework for building APIs with high performance and easy deployment.

Streamlit: Python library for creating interactive web apps for machine learning and data science projects.

LangChain: Framework used for implementing the project with LangServe enabled for application tracing.

Lang Chain Expression Language (LCEL): Implements a chain prompt_template|model|output_parser for enhanced functionality.

LLM Model: Gemma2-9b-It from Groq. 

# Features:
Translation Endpoint: Accepts requests to translate text into specified languages.

Interactive UI: Streamlit-based frontend provides a user-friendly interface for translation input and display.

LangServe Tracing: Enables application tracing for monitoring and performance optimization.

# Installation:
**Clone the repository:**

git clone https://github.com/your-username/your-repository.git

cd your-repository

**Install dependencies:**

pip install -r requirements.txt

**Usage:**

**Start the FastAPI server:**

python server.py

**Launch the Streamlit UI:**

streamlit run client.py

**Open your browser and navigate to http://localhost:8501 to access the application.**

**Example:**

Input the target language and text to translate.

Click on the "Translate" button.

View the translated text displayed on the UI.
