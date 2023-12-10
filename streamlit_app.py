from openai import OpenAI
import streamlit as st

st.set_page_config(page_title="Assistente Virtual de Postagem", page_icon="🎨", layout="wide", initial_sidebar_state="collapsed")

with st.sidebar:
    st.title("Assistente Virtual de Postagem 🎨")
    if 'OPENIA_API_KEY' in st.secrets:
        st.success('Chave de API carregada com sucesso!', icon="✅")
        OpenAI.api_key = st.secrets['OPENIA_API_KEY']
    else:
        OpenAI.api_key = st.text_input('Insira sua chave OpenIA aqui...', type="password")
        if not (OpenAI.api_key.startswith('sk-') and len(OpenAI.api_key) == 51):
            st.error('Chave de API inválida! 😢')
        else:
            st.success('Chave de API carregada com sucesso!', icon="✅")
    st.divider()
    
# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = f"Echo: {prompt}"
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})