from dotenv import load_dotenv 
load_dotenv()              # loading all the environmnent variables

import streamlit as st     # For frontend
import os

import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini Pro model and get response
model=genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

# Initiallize stremlit app
st.set_page_config(page_title="Q&A Demo", page_icon="icon.png")
st.header("Gemini LLM Application")

input=st.text_input("Input: ",key="input")
submit=st.button("Ask the question")

# When submit is clicked
if submit:
    response=get_gemini_response(input)
    st.subheader("The Response is ")
    st.write(response)