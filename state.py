from typing import TypedDict, Optional
from schemas.review import PaperReview

class PaperReviewState(TypedDict):
    # --- inputs ---
    pdf_path: str
    user_query: str

    # --- parser agent output ---
    title: str
    abstract: str
    sections: dict[str, str]      # e.g. {"introduction": "...", "methods": "..."}
    raw_text: str

    # --- claim agent output ---
    claims: list[str]

    # --- retrieval agent output ---
    related_papers: list[dict]    # [{"title": ..., "abstract": ..., "url": ...}]

    # --- critique agent output ---
    critique_notes: dict[str, str]  # {"novelty": "...", "methodology": "..."}

    # --- final output ---
    final_review: Optional[PaperReview]
    error: Optional[str]