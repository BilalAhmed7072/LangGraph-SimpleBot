import os
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, START , END
from langchain.messages import AIMessage , HumanMessage
from typing import Dict, TypedDict , List ,Union
from dotenv import load_dotenv

load_dotenv()

class StateAgent(TypedDict):
    messages: List[Union[AIMessage,HumanMessage]]

llm = ChatOpenAI(model="gpt-4o")

def process(state:StateAgent)->StateAgent:
    """ this node will do the action"""
    response = llm.invoke(state["messages"])
    state["messages"].append(AIMessage(content=response.content))
    print(f"\n AI: {response.content}")
    return state


graph = StateGraph(StateAgent)
graph.add_node("process",process)
graph.add_edge(START,"process")
graph.add_edge("process",END)

agent = graph.compile()


conversation_history=[]
user_input = input("enter:")
while user_input != "exit":
    conversation_history.append(HumanMessage(content=user_input))
    result = agent.invoke({"messages":conversation_history})
    conversation_history = result["messages"]
    user_input = input("enter:")



with open("logging.txt", "w") as file:
    file.write("your conversation log:")
    for message in conversation_history:
        if isinstance(message,HumanMessage):
           file.write(f"you:{message.content}\n")
        elif isinstance(message,AIMessage):
            file.write(f"AI: {message.content}")
    file.write("end of conversation")\

print("Conversation saved to logging.txt")
        
