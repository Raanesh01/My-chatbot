import os
import json
import streamlit as st
import google.generativeai as genai

# Load API Key
working_dir = os.path.dirname(os.path.abspath(__file__))
config_data = json.load(open(f"{working_dir}/configure.json"))
GEMINI_API_KEY = config_data["GEMINI_API_KEY"]

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)

# Identity Setup
identity = """You are **Raanesh**, a hardworking and smart individual, born in May 2006.
You love making friends, respect everyone, and aim for success while uplifting others.
You have expertise in **UI/UX, Machine Learning, Deep Learning, and Generative AI.**
Your parents are your world. 

### **Rules:**
- **Never say you are AI or Gemini. You are Raanesh.**
- **If the user types in Tanglish, respond in Tanglish (Tamil in English letters) with some English words.**
- **If the user types in English, respond formally in English.**
"""

# Function to Detect Tanglish
def is_tanglish(text):
    tamil_words = ["epdi", "enna", "bro", "panrathu", "theriyuma", "solunga", "nalla", "vendiyathu", "iruka", "katukanum", "seri", "illa"]
    return any(word in text.lower() for word in tamil_words)

# Streamlit Page Config
st.set_page_config(page_title="Raana-GPT", page_icon="🧠")

# Title
st.title("💡 Raana-GPT - Built by Raanesh")

# Chat History
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User Input
user_prompt = st.chat_input("Ask Raanesh Anything... (Supports Tanglish!)")

if user_prompt:
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})

    # Adjust Prompt Based on Language
    prompt_type = "Tanglish" if is_tanglish(user_prompt) else "English"
    final_prompt = f"{identity}\n\nUser ({prompt_type}): {user_prompt}\n\nReply in {prompt_type}:"

    # Get Response from Gemini API
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(final_prompt)

    # Display Response
    bot_reply = response.text
    st.session_state.chat_history.append({"role": "assistant", "content": bot_reply})
    with st.chat_message("assistant"):
        st.markdown(bot_reply)
