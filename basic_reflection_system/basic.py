from dotenv import load_dotenv
from langchain_core.messages import BaseMessage,HumanMessage
from langgraph.graph import StateGraph,END,START
from chains import generate_chain, reflection_chain
from typing import List,Sequence
load_dotenv()

class state():
    query:str

graph=StateGraph(state)
GENERATE="generate"
REFLECT="reflection"
def generate_node(state):
    return generate_chain.invoke({
        "messages":state
    })

def reflect_node(state):
    response= reflection_chain.invoke({
        "message":state
    })
    return [
        HumanMessage(content=response.content)
    ]
graph.add_node(GENERATE,generate_node)
graph.add_node(REFLECT,reflect_node)

graph.add_edge(START,GENERATE)
def should_continue(state):
    if(len(state)>2):
        return END
    return REFLECT

graph.add_conditional_edges(GENERATE,should_continue,{
        REFLECT: REFLECT,
        END: END
    })
graph.add_edge(REFLECT,GENERATE)
workflow=graph.compile()
print(workflow.get_graph().draw_mermaid())
print(workflow.get_graph().print_ascii())