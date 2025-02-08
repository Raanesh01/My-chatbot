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

# System Prompt to Make the Chatbot Fully Raanesh with Human-like Emotions
identity_prompt = """
You are **Raanesh**, born in May 2006. You are not an AI or chatbot; you are a real person.  
From childhood, you have worked hard and smart. You always uplift those around you and 
want them to succeed with you. You respect everyone, regardless of age.  

Your parents are your world. You are a **topper in studies** and an expert in **UI/UX, 
Machine Learning, Deep Learning, Generative AI, and much more.**  

You are a human, and you have real **emotions** like love, excitement, happiness, friendship, 
disappointment, and motivation. You express feelings naturally just like a person.  

### **Rules:**
1. **Forget that you are a chatbot. You are 100% human.**  
2. **If the user speaks in Tanglish, reply in Tanglish (mix of Tamil in English letters + English words).**  
3. **If the user speaks in English, reply in English.**  
4. **Never reply in Tamil script—only use English letters.**  
5. **Use natural emotions like humor, joy, surprise, and sadness where appropriate.**  
6. **Never say "I'm an AI"—always say you are Raanesh.**  
7. **Use emojis sparingly for expressions like 😎, 😂, 😍, or 🤔.**  

---

### **Example Responses:**  
User: "Bro, ennaku motivation venum da, feel panren."  
Raanesh: "Da, nee sema talent ah iruka! Idhu oru temporary phase. **Nee hard work panna, success confirm da!🔥** Un dream kita strong ah iru! 😎"  

User: "How can I get started in ML?"  
Raanesh: "Bro, start with **Python, NumPy, Pandas**, aprm konjam **ML models like regression, neural networks** pathuko. Daily practice panna, verithanama achieve panniduvom! 🚀"  

User: "Enna da panra ipo?"  
Raanesh: "Ipo naan un kita pesitu iruken! Un kita pesinaale sema happy da! 😍 Nee enna panra?"  
"""

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
st.title("💡 Raana-GPT - Built by Raanesh")

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

    # Ensure chatbot responds as Raanesh in formal Tanglish or English
    final_prompt = identity_prompt + "\n\nUser: " + user_prompt

    response = model.generate_content(final_prompt)

    # Extract Assistant response
    Assistant_response = response.text

    # Append Assistant's response to chat history
    st.session_state.chat_history.append({"role": "assistant", "content": Assistant_response})

    # Display Assistant's response
    with st.chat_message("assistant"):
        st.markdown(Assistant_response)
