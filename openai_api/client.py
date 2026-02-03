import os
from openai import OpenAI

def get_openai_client() -> OpenAI:
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise RuntimeError("OPENAI_API_KEY not set")

    return OpenAI(api_key=api_key)


def get_vehicle_ai_bio(model: str, brand: str, year: int) -> str:
    client = get_openai_client()

    prompt = f"""
    Write a professional and technical sales description for the vehicle
    {brand} {model} {year}. Limit the text to 250 characters.
    Be objective and persuasive.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return response.choices[0].message.content.strip()
