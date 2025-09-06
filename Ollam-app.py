import os
from dotenv import load_dotenv

from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser



load_dotenv()

# langsmith tracking
os.environ['LANGCHAIN_API_KEY']=os.getenv("LANGCHAIN_API_KEY")
os.environ['LANGCHAIN_TRACING_V2']="true"
os.environ['LANGCHAIN_PROJECT']=os.getenv("LANGCHAIN_PROJECT")


prompt=ChatPromptTemplate([
    ("system","you are a helpful assistant. please respond to the question asked"),
    ("user","Question: {question}")
])


#streamlit app
st.title("Ollama LLM with Langchain")
st.write("This is a simple app that uses the Ollama LLM with Langchain.")

input_text=st.text_input("How can i help you?")

llm=Ollama(model="gemma3:1b")
OutputParser=StrOutputParser()

chain=prompt |llm | OutputParser

if input_text:
    with st.spinner("Fetching answer..."):
        response=chain.invoke({"question":input_text})
        st.write(response)