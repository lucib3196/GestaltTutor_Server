from typing import List
from pydantic import BaseModel


class PageRange(BaseModel):
    start_page: int
    end_page: int


class LectureMeta(BaseModel):
    lecture_title: str
    lecture_summary: str
    core_topics: List[str]
    learning_objectives: List[str]
    assumed_prerequisites: List[str]
    lecture_type: str


class Derivation(BaseModel):
    derivation_title: str
    derivation_stub: str
    steps: List[str]
    reference: PageRange
