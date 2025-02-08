import os
import json
import streamlit as st
import google.generativeai as genai

# Load API Key from configure.json
working_dir = os.path.dirname(os.path.abspath(__file__))
config_data = json.load(open(f"{working_dir}/configure.json"))
GEMINI_API_KEY = config_data["GEMINI_API_KEY"]

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)

# Configure Streamlit Page
st.set_page_config(
    page_title="Raana-GPT",
    page_icon="🧠",
    layout="centered"
)

# Initialize chat session in Streamlit
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Streamlit Page Title
st.title("💡 Raana-GPT")

# Display Chat History
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input field for user's message
user_prompt = st.chat_input("Ask Raanesh Anything...")

if user_prompt:
    # Add user's message to the chat and display
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})

    # Send user's message to Gemini API and get response
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(user_prompt)

    # Extract assistant response
    Assistant_response = response.text

    # Append Assistant's response to chat history
    st.session_state.chat_history.append({"role": "assistant", "content": Assistant_response})

    # Display Assistant's response
    with st.chat_message("assistant"):
        st.markdown(Assistant_response)


