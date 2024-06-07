
import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
from streamlit_mic_recorder import speech_to_text
import IA_R
from datetime import datetime


with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['pre-authorized']
)



authenticator.login('sidebar')

if st.session_state["authentication_status"]:
    authenticator.logout()
    st.write(f'Welcome *{st.session_state["name"]}*')
elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')


st.title('Welcome to the medical scribe')

if st.session_state["authentication_status"] is None:
    st.header("please login or register to continue to continue")

if st.session_state["authentication_status"]:
    state = st.session_state


    if 'text_received' not in state:
        state.text_received = []
        

    c1, c2 = st.columns(2)
    with c1:
        st.write("Record your medical consultation or upload file")
    with c2:
        text = speech_to_text(language='en', use_container_width=True, just_once=True, key='STT')
        current_datetime = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        str_current_datetime = str(current_datetime)
        
    
    if text:
        consultation = IA_R.meeting_minutes(text)
        IA_R.save_as_docx(consultation, f"{str_current_datetime}")
        state.text_received.append(consultation)


   

    for consultation in state.text_received:
        st.markdown(consultation)
       


    