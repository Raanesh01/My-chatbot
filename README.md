# My-chatbot
This is a simple yet powerful AI chatbot built using Google's Gemini API and Streamlit. It allows users to have interactive conversations with an AI assistant, leveraging Google's cutting-edge AI models.

## Features

1) Powered by Google's Gemini API for intelligent responses.
2) Interactive UI built with Streamlit for a smooth user experience.
3) Easy to set up & deploy on platforms like Streamlit Cloud, Render,Heroku or Hugging Face Spaces.
4) Secure API Key Handling – Users must provide their own Gemini API key.

##  Installation & Setup

### Clone the repository :

git clone https://github.com/Raanesh01/My-Chatbot.git


### Install dependencies :

pip install -r requirements.txt


### Set up your Gemini API key :

Get your API key from Google AI Studio.

Create a config.json file in the project directory and add

{
  "GEMINI_API_KEY": "your_api_key_here"
}


###  Run the chatbot :

streamlit run main.py


## Deployment Options

You can deploy this chatbot on:

1) Streamlit Cloud (Recommended).
2) Render.
3) Hugging Face Spaces.
4) Heroku
