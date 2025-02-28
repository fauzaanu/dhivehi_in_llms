import os

import instructor
from anthropic import Anthropic
from dotenv import load_dotenv


def ask_llm(system_prompt, prompt, model, max_tokens, resp_model):
    load_dotenv()

    client = instructor.from_anthropic(Anthropic(
        api_key=os.getenv('ANTHROPIC_API_KEY'),
    ))

    resp = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        messages=[
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": prompt,
            }
        ],
        response_model=resp_model,
    )
    return resp
