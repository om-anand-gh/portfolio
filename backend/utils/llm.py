from django.conf import settings

from openai import AzureOpenAI

EMBEDDING_MODEL = settings.AZURE_OPENAI_EMBEDDING_DEPLOYMENT
CHAT_MODEL = settings.AZURE_OPENAI_CHAT_DEPLOYMENT

llm_client = AzureOpenAI(
    api_key=settings.AZURE_OPENAI_API_KEY,
    api_version="2024-10-21",
    azure_endpoint=settings.AZURE_OPENAI_ENDPOINT,
)


def generate_embeddings(texts: list[str] | str) -> list[list[float]]:
    """
    Takes a list of strings and returns a list of corresponding embeddings.
    """
    if not texts:
        return []

    response = llm_client.embeddings.create(
        input=texts,
        model=EMBEDDING_MODEL,
    )

    return [item.embedding for item in response.data]
