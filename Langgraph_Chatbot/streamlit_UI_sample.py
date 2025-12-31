import streamlit as st 

with st.chat_message('user'):
    st.text('hi')

with st.chat_message('assistant'):
    st.text('How can I help You?')

user_input = st.chat_input('Type Here')


if user_input:
    with st.chat_message('user'):
        st.text(user_input)