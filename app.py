import os
import requests
import streamlit as st

MODEL = os.getenv('OLLAMA_MODEL', 'gemma3:4b')
OLLAMA_URL = os.getenv('OLLAMA_BASE_URL', 'http://localhost:11434').rstrip('/')

st.set_page_config(page_title='DostStudy', page_icon='📚', layout='centered')
st.title('📚 DostStudy')
st.caption('Private AI study buddy powered by Gemma 3 + Ollama')

if 'messages' not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    language = st.selectbox('Explanation style', ['Simple English', 'Hinglish', 'Hindi'])
    level = st.selectbox('Difficulty', ['Beginner', 'School', 'Exam'])
    mode = st.radio('Mode', ['Ask Doubt', 'Explain', 'Summarize', 'Quiz'])
    st.caption(f'Model: {MODEL}')
    if st.button('Clear chat'):
        st.session_state.messages = []
        st.rerun()

def ask_local(prompt):
    system = f'You are DostStudy, a friendly private study assistant. Preferred language: {language}. Level: {level}. Be accurate and clear. Mode: {mode}.'
    payload = {'model': MODEL, 'stream': False, 'messages': [{'role': 'system', 'content': system}, {'role': 'user', 'content': prompt}]}
    try:
        response = requests.post(f'{OLLAMA_URL}/api/chat', json=payload, timeout=180)
        response.raise_for_status()
        return response.json()['message']['content']
    except requests.exceptions.ConnectionError:
        return '⚠️ Ollama is not reachable. Run: ollama pull gemma3:4b'
    except Exception as exc:
        return f'⚠️ Ollama error: {exc}'

for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

prompt = st.chat_input('Ask DostStudy a study question...')
if prompt:
    st.session_state.messages.append({'role': 'user', 'content': prompt})
    with st.chat_message('user'):
        st.markdown(prompt)
    with st.chat_message('assistant'):
        with st.spinner('Thinking locally...'):
            answer = ask_local(prompt)
        st.markdown(answer)
    st.session_state.messages.append({'role': 'assistant', 'content': answer})
