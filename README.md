# LLM Performance for Dhivehi

Simple performance comparison scripts to compare the performance of different LLMs for Dhivehi.

Currently, all relevant models from anthropic are added, Next step would be to add the models from Google, and finally
openai (O1 has some hope, and GPT-4.5 speaks broken dhivehi)

### Installation

`uv sync`

### Usage

1. Define a pydantic schema for the output (structured output)
2. call the benchmark_models function
    - benchmark_models(prompt, system_prompt, response_model, output_file='benchmark_results.txt')