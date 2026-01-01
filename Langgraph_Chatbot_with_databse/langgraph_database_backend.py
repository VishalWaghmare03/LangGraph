from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage
from langchain_openai import ChatOpenAI
# from langgraph.checkpoint.memory import InMemorySaver
from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.graph.message import add_messages
from langchain_core.messages import BaseMessage, HumanMessage
from dotenv import load_dotenv
import sqlite3
import os

load_dotenv()

llm = ChatOpenAI(model="gpt-4.1-nano")

class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

def chat_node(state: ChatState):
    messages = state['messages']
    response = llm.invoke(messages)
    return {"messages": [response]}

# sqlite work with only single thread,same database ko ham alag alag thread ke sath use karenge
# that's why check_same_thread=False
conn = sqlite3.connect(database='chatbot.db', check_same_thread=False)

# Checkpointer
checkpointer = SqliteSaver(conn=conn)

graph = StateGraph(ChatState)
graph.add_node('chat_node', chat_node)
graph.add_edge(START, 'chat_node')
graph.add_edge('chat_node', END)

chatbot = graph.compile(checkpointer=checkpointer)


# # Test
# CONFIG = {'configurable':{'thread_id': 'thread-2'}}
# response = chatbot.invoke(
#                 {'messages':[HumanMessage(content="what is my name?")]},
#                 config = CONFIG
#             )

# print(response)


### see the checkpoints
def retrieve_all_threads():
    all_threads = set()
    for checkpoint in checkpointer.list(None):
        all_threads.add(checkpoint.config['configurable']['thread_id'])
    return list(all_threads)

# for th in retrieve_all_threads():
#     print(th)