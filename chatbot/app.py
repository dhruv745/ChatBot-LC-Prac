from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
st.title("ChatBot with LangChain and Streamlit")

prompt = ChatPromptTemplate.from_messages([("system", "You're a helpful assistant. Answer the Natural Language Answer with accuracy"), 
                                          ("user", "Question:{question}")])

llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

input_text = st.text_input("Enter your question:")
output_parser = StrOutputParser()

chain = prompt | llm | output_parser

if st.button("Get Answer"):
    if input_text:
        response = chain.invoke({"question": input_text})
        st.write("Answer:", response.content)
    else:
        st.write("Please enter a question.")

# To run this app, use the command: streamlit run app.py