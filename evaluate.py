"""
LLM based evaluation for how each model performed
"""
from typing import List

from ask import ask_llm
from pydantic import BaseModel

from graph import generate_graph


class ModelPerformance(BaseModel):
    model_name: str
    dhivehi_grammer_rating_out_of_10: int
    dhivehi_sentence_structure_rating_out_of_10: int
    dhivehi_spelling_accuracy_out_of_10: int
    dhivehi_vocabulary_richness_out_of_10: int
    dhivehi_word_choice_accuracy_out_of_10: int
    dhivehi_readability_out_of_10: int
    dhivehi_fluency_out_of_10: int
    dhivehi_coherence_out_of_10: int
    dhivehi_text_complexity_out_of_10: int
    dhivehi_formality_appropriateness_out_of_10: int
    dhivehi_punctuation_accuracy_out_of_10: int
    dhivehi_consistency_out_of_10: int
    dhivehi_sentence_variation_out_of_10: int
    dhivehi_lexical_diversity_out_of_10: int
    dhivehi_redundancy_reduction_out_of_10: int
    dhivehi_paragraph_structure_out_of_10: int
    dhivehi_context_relevance_out_of_10: int
    dhivehi_cultural_sensitivity_out_of_10: int
    dhivehi_synonym_usage_out_of_10: int
    dhivehi_technical_accuracy_out_of_10: int
    dhivehi_clarity_out_of_10: int
    dhivehi_tone_consistency_out_of_10: int
    dhivehi_overall_quality_out_of_10: int


class BenchMark(BaseModel):
    benchmarks: List[ModelPerformance]


with open('dhivehi_results.txt', 'r', encoding="utf-8") as f:
    dhivehi_results = f.read()
    PROMPT = dhivehi_results


ev = ask_llm(
    system_prompt="You are a Dhivehi language expert.",
    prompt=PROMPT + "Rate the performance of the models based on how they answered. Be ultra strict. Rate it. Benchmark it.",
    model="claude-3-7-sonnet-20250219",
    max_tokens=8000,
    resp_model=BenchMark,
)

with open("model_ratings.txt", "w", encoding="utf-8") as f:
    for model in ev.benchmarks:
        f.write(f"Model: {model.model_name}\n")
        f.write("-" * (len(model.model_name) + 7) + "\n")

        for key, value in model.model_dump().items():
            if key != "model_name":
                formatted_key = key.replace("dhivehi_", "").replace("_out_of_10", "").replace("_", " ").capitalize()
                f.write(f"{formatted_key}: {value}/10\n")

        f.write("\n")

# Generate visualization
generate_graph(ev)
