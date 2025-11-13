from typing import Dict, TypedDict , List
from langgraph.graph import StateGraph, START , END
from langchain.messages import HumanMessage , AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

class AgentState(TypedDict):
    messages: List[HumanMessage]


llm = ChatOpenAI(model="gpt-4o-mini")
conversation_history: List[HumanMessage]=[]

def process(state:AgentState)->AgentState:
    """this is the node to perform action"""
    conversation_history.extend(state["messages"])
    response = llm.invoke(conversation_history)
    conversation_history.append(AIMessage(content=response.content))
    print(f" this is response : {response.content}")
    return state


graph = StateGraph(AgentState)

graph.add_node("process node", process)
graph.add_edge(START, "process node")
graph.add_edge("process node", END)
agent = graph.compile()
    

while True:
    user_input= input("You:")
    if user_input.lower()=="exit":
        break
    agent.invoke({"messages":[HumanMessage(content=user_input)]})
