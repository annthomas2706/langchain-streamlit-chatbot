# Import Streamlit for UI
import streamlit as st

# Import Groq LLM through LangChain
from langchain_groq import ChatGroq

# Import function to load environment variables
from dotenv import load_dotenv


# Load variables from .env file (GROQ_API_KEY)
load_dotenv()


# Configure Streamlit page
st.set_page_config(
    page_title="Chatbot",      # Browser tab title
    page_icon="🤖",            # Browser tab icon
    layout="centered",         # Center page content
)

# Display page heading
st.title("💬 Generative AI Chatbot")


# Create chat history only during first run
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# Display previous messages stored in session state
for message in st.session_state.chat_history:

    # Create user/assistant chat bubble
    with st.chat_message(message["role"]):

        # Display message text inside bubble
        st.markdown(message["content"])


# Create Groq LLM object
llm = ChatGroq(

    # LLM model name
    model="llama-3.3-70b-versatile",

    # Controls randomness
    # 0 = deterministic
    # 1 = creative
    temperature=0.0,
)


# Create chat input box at bottom of page
user_prompt = st.chat_input("Ask Chatbot...")


# Execute only when user submits a question
if user_prompt:

    # Show user message immediately on UI
    st.chat_message("user").markdown(user_prompt)

    # Save user message into chat history
    st.session_state.chat_history.append(
        {
            "role": "user",
            "content": user_prompt
        }
    )

    # Send system prompt + entire chat history to LLM
    response = llm.invoke(
        input=[
            {
                "role": "system",
                "content": "You are a helpful assistant"
            },

            # Unpack all chat history messages
            *st.session_state.chat_history
        ]
    )

    # Extract text response from AIMessage object
    assistant_response = response.content

    # Store assistant response in history
    st.session_state.chat_history.append(
        {
            "role": "assistant",
            "content": assistant_response
        }
    )

    # Display assistant response in assistant bubble
    with st.chat_message("assistant"):
        st.markdown(assistant_response)