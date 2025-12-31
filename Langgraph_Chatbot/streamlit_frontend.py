import streamlit as st 
from langgraph_backend import chatbot
from langchain_core.messages import BaseMessage, HumanMessage

user_input = st.chat_input('Type here')

# when we use simple python-dictionary, and when click enter, the whole code rerun and we get empty dictionary
# that's why we use streamlit dictionary, session_state
# message_history = []
# {'role':'user','content':'hi'}
# {'role':'assistant','content':'hello'}

if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

# loading the conversation history
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])

# {'role':'user','content':'hi'}
# {'role':'assistant','content':'hello'}

if user_input:
    # first add the message to message_history
    st.session_state['message_history'].append({'role':'user','content':user_input})
    with st.chat_message('user'):
        st.text(user_input)

    CONFIG = {'configurable':{'thread_id': 'thread-1'}}
    response = chatbot.invoke({'messages':[HumanMessage(content=user_input)]}, config=CONFIG)
    ai_message = response['messages'][-1].content
    # first add the message to message_history
    st.session_state['message_history'].append({'role':'assistant','content':ai_message})
    with st.chat_message('assistant'):
        st.text(ai_message)