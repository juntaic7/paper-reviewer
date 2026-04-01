from langgraph.graph import StateGraph, END
from state import PaperReviewState
from agents.parser_agent import parser_agent
from agents.claim_agent import claim_agent
from agents.retrieval_agent import retrieval_agent
from agents.critique_agent import critique_agent
from agents.summary_agent import summary_agent

def build_graph() -> StateGraph:
    g = StateGraph(PaperReviewState)

    # register nodes
    g.add_node("parser",    parser_agent)
    g.add_node("claim",     claim_agent)
    g.add_node("retrieval", retrieval_agent)
    g.add_node("critique",  critique_agent)
    g.add_node("summary",   summary_agent)

    # edges
    g.set_entry_point("parser")
    g.add_edge("parser",    "claim")
    g.add_edge("parser",    "retrieval")   # parallel branch
    g.add_edge("claim",     "critique")
    g.add_edge("retrieval", "critique")
    g.add_edge("critique",  "summary")
    g.add_edge("summary",   END)

    return g.compile()