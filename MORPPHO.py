import streamlit as st
import pandas as pd
#fit_ex=pd.read_csv('C:/Users/pc/Desktop/datasets/fitness_exercises.csv')
#st.dataframe(fit_ex) 

from hugchat import hugchat

from hugchat.login import login

st.set_page_config(page_title="😉📧Hugchat")

with st.sidebar:
    st.title("😉📧Hugchat")
    if ('EMAIL' in st.secrets) and ('PASS' in st.secrets):
        st.sucess('HuggingFace Login credentials already provided!', icon='😏')
        hf_email=st.secrets['EMAIL']
        hf_pass=st.secrets['PASS']
    else:
        hf_email=st.text_input('Enter E-mail', type='password')
        hf_pass=st.text_input('Enter pasword', type='password')
        if not (hf_email and hf_pass):
            st.warning('Please enter your crednetials')
        else:
            st.sucess('Proceed to entering your prompt message!', icon="👉")
    if "messages" not in st.session_state_keys():
        st.session_state.messages=[{'role':'assistant',"content":'How may I help you'}]
    
    for message in st.session_state.messages:
        with st.chat_message(message['role']):
            st.write(message['content'])
    def generate_response(prompt_input, email, passwd):
        sign=login(email, passwd)
        cookies=sign.login()
        chatbot=hugchat.ChatBot(cookies=cookies.get_dict())
        return chatbot.chat(prompt_input)
    if prompt:=st.chat_input(disabled=not (hf_email and hf_pass)):
        st.session_state.message.append({'role':'user', 'content':prompt})
        with st.chat_message('user'):
            st.write(prompt)
    if st.session_state.messages[-1]['role']!="assistant":
        with st.chat_messages('assistant'):
            with st.spinner('Thinking...'):
                response=generate_response(prompt, hf_email, hf_pass)
            st.write(response)
        message={'role':'assistant','content':response}
        st.session_state.messages.append(message)






                    