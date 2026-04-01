import asyncio
from dotenv import load_dotenv
from graph import build_graph
from state import PaperReviewState

load_dotenv()

async def main(pdf_path: str, query: str):
    graph = build_graph()

    initial_state: PaperReviewState = {
        "pdf_path": pdf_path,
        "user_query": query,
        "title": "",
        "abstract": "",
        "sections": {},
        "raw_text": "",
        "claims": [],
        "related_papers": [],
        "critique_notes": {},
        "final_review": None,
        "error": None,
    }

    async for event in graph.astream(initial_state):
        node_name = list(event.keys())[0]
        print(f"✓ {node_name} complete")

    print("\nDone.")

if __name__ == "__main__":
    asyncio.run(main("paper.pdf", "Is the evaluation rigorous?"))