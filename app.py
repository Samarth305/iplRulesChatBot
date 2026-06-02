import streamlit as st
from main import create_pipeline
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
os.environ["HF_HUB_DISABLE_SYMLINKS"] = "1"

st.set_page_config(page_title="IPL Rules Chatbot", page_icon="🏏")

st.title("🏏 IPL Rules Chatbot")
st.write("Ask me anything about the IPL playing conditions, DRS, Super Overs, and more!")

# Initialize the pipeline in session state so it doesn't reload on every interaction
if "pipeline" not in st.session_state:
    with st.spinner("Initializing AI Pipeline..."):
        st.session_state.pipeline = create_pipeline()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What are the rules for a super over?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Get AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = st.session_state.pipeline.process_query(prompt)
            st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
