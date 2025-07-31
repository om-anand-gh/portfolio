from pydantic import BaseModel
from typing import List

from experiences.models import Keyword

from .instructor import extract_structured_data


class BatchKeywordOutput(BaseModel):
    keywords: List[List[str]]  # One list per line


def extract_keywords_for_lines(lines: List[str]) -> List[List[str]]:
    existing_keywords = set(keyword.name for keyword in Keyword.objects.all())

    prompt = (
        "You are given a list of text lines. For each line, extract 3-5 short, meaningful keywords that best represent the content of that line.\n\n"
        "When possible, prefer to use keywords from the following list of existing keywords:\n"
        f"{sorted(existing_keywords)}\n\n"
        "If no suitable existing keywords apply, you may suggest new ones.\n\n"
        "Return the result as a JSON list of lists of strings, where each inner list corresponds to the keywords for one line.\n\n"
        "Example output:\n"
        '[["python", "machine learning", "data science"], ["docker", "kubernetes", "devops"]]'
    )

    joined_lines = "\n".join(f"{i+1}. {line}" for i, line in enumerate(lines))

    result = extract_structured_data(
        joined_lines, BatchKeywordOutput, system_prompt=prompt
    )

    cleaned_keywords = [
        [kw.strip().lower() for kw in keyword_list] for keyword_list in result.keywords
    ]
    return cleaned_keywords
