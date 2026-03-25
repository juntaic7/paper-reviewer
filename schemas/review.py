from pydantic import BaseModel, Field
from typing import Optional

class SectionScore(BaseModel):
    score: float = Field(..., ge=1, le=5, multiple_of=0.5)
    justification: str

class PaperReview(BaseModel):
    title: str
    summary: str
    novelty: SectionScore
    methodology: SectionScore
    experiments: SectionScore
    advantage: str
    weakness: str
    overall_score: float = Field(..., ge=1, le=5, multiple_of=0.5)
    recommendation: str  # "accept" | "conditional_accept" | "reject"
    related_papers: list[str] = []