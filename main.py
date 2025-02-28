import time
from typing import List

from pydantic import ValidationError

from ask import ask_llm

from pydantic import BaseModel


def benchmark_models(prompt, system_prompt, response_model, output_file='benchmark_results.txt'):
    """
    Benchmark different models with a single prompt and flexible response model support.

    Args:
        prompt: The prompt to test
        response_model: The Pydantic model to use for structured responses
        output_file: The file to write benchmark results to
    """
    models_to_test = [
        {
            'name': 'claude-3-5-sonnet-20241022',
            'func': ask_llm,
            'system_prompt': system_prompt,
        },
        {
            'name': 'claude-3-7-sonnet-20250219',
            'func': ask_llm,
            'system_prompt': system_prompt,
        },
        {
            'name': 'claude-3-5-haiku-20241022',
            'func': ask_llm,
            'system_prompt': system_prompt,
        },
        {
            'name': 'claude-3-haiku-20240307',
            'func': ask_llm,
            'system_prompt': system_prompt,
        },
    ]

    # Initialize the output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("Benchmark Results\n")
        f.write("================\n\n")
        f.write(f"Prompt: {prompt}\n\n")

    print(f"-----\nPrompt: {prompt}\n")

    for model_info in models_to_test:
        model_name = model_info['name']
        request_func = model_info['func']
        system_prompt = model_info['system_prompt']

        try:
            start_time = time.time()
            # Make the request with the provided response model
            response = request_func(
                system_prompt=system_prompt,
                prompt=prompt,
                model=model_name,
                max_tokens=1000,  # Increased for potentially longer responses
                resp_model=response_model,
            )
            elapsed = time.time() - start_time

            # Print results to console
            print(f"Model: {model_name}")
            print(f"Time taken (s): {elapsed:.2f}")

            # Handle the response generically by converting to dict
            response_dict = response.model_dump()
            print(f"Response: {response_dict}\n")

            # Append to the output file
            with open(output_file, 'a', encoding='utf-8') as f:
                f.write(f"Model: {model_name}\n")
                f.write(f"Time taken (s): {elapsed:.2f}\n")
                f.write("Response:\n")

                # Format the response nicely based on the model structure
                for key, value in response_dict.items():
                    f.write(f"  {key}:\n")
                    if isinstance(value, list):
                        for item in value:
                            f.write(f"    - {item}\n")
                    else:
                        f.write(f"    {value}\n")
                f.write("\n")

        except ValidationError as ve:
            error_msg = f"Model: {model_name} - ValidationError: {ve}\n"
            print(error_msg)
            with open(output_file, 'a', encoding='utf-8') as f:
                f.write(error_msg + "\n")
        except Exception as e:
            error_msg = f"Model: {model_name} - Error: {e}\n"
            print(error_msg)
            with open(output_file, 'a', encoding='utf-8') as f:
                f.write(error_msg + "\n")

    print("=====\n")
    with open(output_file, 'a', encoding='utf-8') as f:
        f.write("=====\n\n")


if __name__ == '__main__':
    class CuriousityRover(BaseModel):
        tags: List[str]
        understood_facts: List[str]
        questions_i_have: List[str]


    SUMMARY_TEXT = """
    At Xiao Ye, Lin has struggled with similar logistics, in addition to price. Although selling burgers brings in new guests, the amount of money each guest spends on burger night is significantly lower than a regular service. That means the restaurant needs to feed many more guests in a night to make the same amount of money, which changes the flow of service as they work to turn tables.
    """

    prompt = f"Read the following text and tell me what you understood: {SUMMARY_TEXT}"
    system_prompt = "KEEP YOUR RESPONSE SHORT AND TO THE POINT AND IN DHIVEHI"
    benchmark_models(prompt=prompt, system_prompt=system_prompt, response_model=CuriousityRover,
                     output_file='dhivehi_results.txt')
