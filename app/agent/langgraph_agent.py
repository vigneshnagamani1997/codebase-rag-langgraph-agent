from langgraph.graph import StateGraph, END
from typing import TypedDict, List
from app.agent.tools.search import search_code
from app.agent.tools.file_reader import read_file
from app.agent.tools.code_analyzer import analyze_code
from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")

class AgentState(TypedDict):
    query: str
    context: List[str]
    steps: int
    answer: str


def decide_tool(state: AgentState):
    prompt = f"""
You are an AI agent.

Decide next action:
- search_code
- read_file
- analyze_code
- finish

Query: {state['query']}
Context: {state['context']}
"""

    response = llm.invoke(prompt).content

    return {"decision": response}


def run_tool(state: AgentState):
    decision = state["decision"]

    if "search_code" in decision:
        result = search_code(state["query"])
    elif "read_file" in decision:
        result = read_file(state["query"])
    elif "analyze_code" in decision:
        result = analyze_code("\n".join(state["context"]))
    else:
        return state

    state["context"].append(str(result))
    state["steps"] += 1
    return state


def should_continue(state: AgentState):
    if state["steps"] > 3:
        return "finish"
    return "continue"


def generate_answer(state: AgentState):
    prompt = f"""
Answer using context:

{state['context']}

Question: {state['query']}
"""

    response = llm.invoke(prompt).content
    state["answer"] = response
    return state


# Graph
graph = StateGraph(AgentState)

graph.add_node("decide", decide_tool)
graph.add_node("act", run_tool)
graph.add_node("answer", generate_answer)

graph.set_entry_point("decide")

graph.add_edge("decide", "act")
graph.add_conditional_edges(
    "act",
    should_continue,
    {
        "continue": "decide",
        "finish": "answer"
    }
)

graph.add_edge("answer", END)

app_graph = graph.compile()


def run_agent(query: str):
    result = app_graph.invoke({
        "query": query,
        "context": [],
        "steps": 0,
        "answer": ""
    })

    return result["answer"]