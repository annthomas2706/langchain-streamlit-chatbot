# Generative AI Chatbot using Streamlit, LangChain & Groq

## Overview

This project is a Generative AI Chatbot built using Streamlit, LangChain, and Groq. It provides a simple conversational interface that allows users to interact with a Large Language Model (LLM) and receive real-time AI-generated responses.

## Features

* Interactive chat interface using Streamlit
* Integration with Groq LLM (Llama 3.3 70B Versatile)
* Conversation history management using Streamlit Session State
* Real-time AI responses
* Environment variable management using python-dotenv
* Clean and responsive user interface

## Tech Stack

* Python
* Streamlit
* LangChain
* Groq
* python-dotenv

## Project Structure

chatbot/
├── chatbot.py
├── .env
├── requirements.txt
└── README.md

## Installation

### Clone the Repository

git clone https://github.com/annthomas2706/langchain-groq-chatbot.git

cd langchain-groq-chatbot

### Install Dependencies

pip install -r requirements.txt

### Configure Environment Variables

Create a .env file and add:

GROQ_API_KEY=your_api_key_here

### Run the Application

streamlit run chatbot.py

## How It Works

1. User enters a question in the chat interface.
2. The query is sent to the Groq LLM through LangChain.
3. Previous conversation history is maintained using Streamlit Session State.
4. The model generates a response.
5. The response is displayed in the chat window.

## Skills Demonstrated

* LLM Integration
* Prompt Engineering
* Conversational AI
* LangChain
* Streamlit Application Development
* API Integration
* Session State Management

## Future Enhancements

* Add Retrieval-Augmented Generation (RAG)
* Document Upload Support
* Multi-LLM Integration (OpenAI, Gemini, Ollama)
* Chat History Persistence
* Streaming Responses


