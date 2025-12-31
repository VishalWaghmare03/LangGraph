from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph.message import add_messages
from langchain_core.messages import BaseMessage, HumanMessage
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatOpenAI(model="gpt-4.1-nano")

class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

def chat_node(state: ChatState):
    messages = state['messages']
    response = llm.invoke(messages)
    return {"messages": [response]}

# Checkpointer
checkpointer = InMemorySaver()

graph = StateGraph(ChatState)
graph.add_node('chat_node', chat_node)
graph.add_edge(START, 'chat_node')
graph.add_edge('chat_node', END)

chatbot = graph.compile(checkpointer=checkpointer)


# initial_state = {
#     'messages': [HumanMessage(content='Which is best city in maharashtra')]
# }

# result = chatbot.invoke(initial_state)['messages'][-1].content



########## We are doing this below streaming code in frontend side ##############
# ref :: https://docs.langchain.com/oss/python/langgraph/streaming#messages

# CONFIG = {'configurable':{'thread_id': 'thread-1'}}


# for message_chunk, metadata in chatbot.stream(
    # {'messages':[HumanMessage(content="What pune is famous?")]},
    # config = CONFIG,
    # stream_mode = 'messages'
# ):
#     if message_chunk.content:
#         print(message_chunk.content, end=" ", flush=True)


# print(type(stream)) ## --> <class 'generator'>



######################################################################

# CONFIG = {'configurable': {'thread_id':'thread-1'}}

# response = chatbot.invoke(
#     {'messages': [HumanMessage(content='Hi my name is Vishal')]},
#     config = CONFIG
# )

# print(chatbot.get_state(config=CONFIG).values['messages'])