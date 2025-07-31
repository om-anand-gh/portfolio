import instructor
from pydantic import BaseModel
from typing import Type, TypeVar

from .llm import CHAT_MODEL
from .llm import llm_client as client

client = instructor.from_provider(f"azure_openai/{CHAT_MODEL}")

T = TypeVar("T", bound=BaseModel)


def extract_structured_data(content: str, model: Type[T], system_prompt: str) -> T:
    response = client.chat.completions.create(
        model=CHAT_MODEL,
        response_model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": content},
        ],
    )
    return response
