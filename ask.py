import os

import instructor
from anthropic import Anthropic
import google.generativeai as genai
from dotenv import load_dotenv
from openai import OpenAI


def ask_llm(system_prompt, prompt, model, max_tokens, resp_model):
    load_dotenv()

    # Check if the model name contains 'gemini'
    if "gemini" in model.lower():
        genai.configure(api_key=os.environ['GEMINI_API_KEY'])
        # Use the Google/Gemini client
        client = instructor.from_gemini(
            client=genai.GenerativeModel(
                model_name=model,  # e.g. "models/gemini-1.5-flash-latest"
            ),
            mode=instructor.Mode.GEMINI_JSON,
        )

        resp = client.messages.create(
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
            response_model=resp_model
        )
        return resp
    elif "deepseek" in model.lower():
        #    OpenAI(api_key=os.getenv("DEEPSEEK_API_KEY"), base_url="https://api.deepseek.com")
        # Use the Deepseek client
        client = instructor.from_openai(
            OpenAI(
                api_key=os.getenv("DEEPSEEK_API_KEY"),
                base_url="https://api.deepseek.com",
            ),
            mode=instructor.Mode.MD_JSON if "reasoner" in model.lower() else instructor.Mode.TOOLS
        )

        # Create structured output
        resp = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            response_model=resp_model,
        )
        return resp




    else:
        # Otherwise default to Anthropic
        client = instructor.from_anthropic(
            Anthropic(
                api_key=os.getenv('ANTHROPIC_API_KEY'),
            )
        )

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
