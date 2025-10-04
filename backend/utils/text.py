import re

def extract_lines(text: str) -> list[str]:
    """
    Splits a paragraph into logical lines based on newlines and periods.

    Rules:
    - Split on `\n` or `. ` (period followed by space).
    - Keep punctuation where appropriate.
    - Strip whitespace and ignore empty results.
    """
    if not text:
        return []

    # Replace newlines with periods for consistency
    text = text.replace('\n', '. ')
    # Use regex to split on periods followed by space or end of line
    raw_lines = re.split(r'\.\s+', text.strip())
    lines = [line.strip() for line in raw_lines if line.strip()]
    return lines
