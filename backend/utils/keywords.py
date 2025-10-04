import logging
from pydantic import BaseModel
from typing import List

from experiences.models import Keyword

from .instructor import extract_structured_data


class BatchKeywordOutput(BaseModel):
    keywords: List[List[str]]  # One list per line

class ExperienceOutput(BaseModel):
    paragraph: str

def extract_keywords_for_lines(lines: List[str]) -> List[List[str]]:
    existing_keywords = set(keyword.name for keyword in Keyword.objects.all())

    prompt = (
        "You are given a list of text lines. For each line, extract 8-10 short, meaningful keywords that best represent the content of that line.\n\n"
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


def clean_experience_paragraph(paragraph: str) -> str:
    """
    Cleans and restructures a paragraph describing an experience so it can be 
    stored as a polished paragraph for the portfolio project.

    Uses an LLM to:
    - Remove redundancy or filler
    - Ensure it's concise and professional
    - Return the result as a single paragraph
    """

    prompt = (
        "You are given a paragraph describing professional experience. "
        "Rewrite it into a clean, concise, professional-style paragraph "
        "suitable for a resume or portfolio. "
        "Remove redundancies, unnecessary filler, and repeated information. "
        "Keep it natural as a single polished paragraph. "
        "Return the result as a JSON object with a field `paragraph`."
    )

    # Call Instructor / LLM and coerce into your Pydantic model
    result: ExperienceOutput = extract_structured_data(
        paragraph, ExperienceOutput, system_prompt=prompt
    )

    logging.debug(f'Converted "{paragraph}"\n to \n "{result.paragraph.strip()}"\n.')

    # Return the cleaned paragraph string
    return result.paragraph.strip()

