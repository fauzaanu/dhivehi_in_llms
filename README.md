# LLM Performance for Dhivehi

Simple performance comparison script to compare the performance of different LLMs for Dhivehi.

Currently, all relevant models from anthropic and google are added. We should add all the other models instructor has
support for to see a more comprehensive comparison.

### Installation
1. Clone the repository
2. Make sure you have uv [installed](https://docs.astral.sh/uv/getting-started/installation/)
3. Run `uv sync --frozen --no-dev`

### Usage

1. Define a pydantic schema for the output (structured output)
2. call the benchmark_models function
    - benchmark_models(prompt, system_prompt, response_model, output_file='benchmark_results.txt')

```python
class CuriousityRover(BaseModel):
    tags: List[str]
    understood_facts: List[str]
    questions_i_have: List[str]


SUMMARY_TEXT = """
At Xiao Ye, Lin has struggled with similar logistics, in addition to price. 
Although selling burgers brings in new guests, the amount of money each guest 
spends on burger night is significantly lower than a regular service. 
That means the restaurant needs to feed many more guests in a night to make
 the same amount of money, which changes the flow of service as they work to turn tables.
"""

prompt = f"Read the following text and tell me what you understood: {SUMMARY_TEXT}"
system_prompt = "KEEP YOUR RESPONSE SHORT AND TO THE POINT AND IN DHIVEHI"
benchmark_models(prompt=prompt, system_prompt=system_prompt, response_model=CuriousityRover,
                 output_file='dhivehi_results.txt')
```

### Output

```text
Benchmark Results
================

Prompt: Read the following text and tell me what you understood: 
    At Xiao Ye, Lin has struggled with similar logistics, in addition to price. Although selling burgers brings in new guests, the amount of money each guest spends on burger night is significantly lower than a regular service. That means the restaurant needs to feed many more guests in a night to make the same amount of money, which changes the flow of service as they work to turn tables.
    

Model: claude-3-5-sonnet-20241022
Time taken (s): 11.28
Response:
  tags:
    - ރެސްޓޯރަންޓް
    - ބިޒްނަސް
    - ލޮޖިސްޓިކްސް
    - ކަސްޓަމަރ ސަރވިސް
  understood_facts:
    - ޝިއާއޯ ޔޭގައި ލިން ވަނީ ލޮޖިސްޓިކްސްގެ ދަތިތަކާ ކުރިމަތިލާންޖެހިފަ
    - ބަރގަރ ވިއްކުމުން އައު ކަސްޓަމަރުން ލިބޭ
    - ބަރގަރ ނައިޓްގައި ކަސްޓަމަރުން ހޭދަކުރާ މިންވަރު މަދު
    - އާމްދަނީ ހޯދުމަށް ގިނަ ކަސްޓަމަރުންނަށް ޚިދުމަތް ދޭންޖެހޭ
  questions_i_have:
    - ޝިއާއޯ ޔޭ އަކީ ކޮން ބާވަތެއްގެ ރެސްޓޯރަންޓެއްތަ؟
    - ބަރގަރ ނައިޓް ބާއްވަނީ ކިތައް ދުވަހުތަ؟
    - ރެސްޓޯރަންޓްގެ އާންމު އަގުތަކަކީ ކޮބާ؟

Model: claude-3-7-sonnet-20250219
Time taken (s): 15.40
Response:
  tags:
    - ރެސްޓޯރަންޓް
    - ވިޔަފާރި
    - ލޮޖިސްޓިކްސް
    - ބަރގަރ ނައިޓް
  understood_facts:
    - ޝިއާއޯ ޔޭގައި ލިން ލޮޖިސްޓިކްސްއާއި އަގުގެ މައްސަލަތަކާ ކުރިމަތިލާންޖެހިފައިވޭ
    - ބަރގަރ ވިއްކުމުން އައު ކަސްޓަމަރުން ލިބުނަސް، އާމްދަނީ މަދުވޭ
    - އާންމު ޚިދުމަތްތަކަށް ވުރެ ބަރގަރ ނައިޓްގައި ކަސްޓަމަރުން ހޭދަކުރާ މިންވަރު މަދު
    - އެއް ވަރެއްގެ ފައިދާ ހޯދުމަށް ގިނަ ކަސްޓަމަރުންނަށް ޚިދުމަތްދޭންޖެހޭ
    - މޭޒުތައް އަވަހަށް ހުސްކުރުމަށް މަސައްކަތްކުރަންޖެހޭ
  questions_i_have:
    - ރެސްޓޯރަންޓުގެ އާންމު ޚިދުމަތުގެ އާމްދަނީއާ ބަރގަރ ނައިޓްގެ އާމްދަނީއާ ހުރި ތަފާތަކީ ކޮބާ؟
    - ރެސްޓޯރަންޓުން މި މައްސަލަ ހައްލުކުރަން ގެންގުޅޭ ވަސީލަތްތަކަކީ ކޮބާ؟
    - ބަރގަރ ނައިޓް ކުރިއަށްގެންދިއުމުގެ ވިޔަފާރި ފައިދާ ލިބޭތޯ؟

Model: claude-3-5-haiku-20241022
Time taken (s): 6.30
Response:
  tags:
    - restaurant
    - business
    - pricing
  understood_facts:
    - Lin's restaurant (Xiao Ye) has introduced burger nights
    - Burger nights attract new customers
    - Customers spend less money during burger nights compared to regular service
    - More customers need to be served to maintain the same revenue
    - Burger nights change the restaurant's service flow and table turnover strategy
  questions_i_have:
    - އާއި ބާރގަރ ނައިޓް އިން އާމްދަނީ އިތުރުވާނެތޯ؟
    - މިއީ ކޮން ބާވަތެއްގެ ގޮންޖެހުމެއްތޯ؟

Model: claude-3-haiku-20240307
Time taken (s): 2.85
Response:
  tags:
    - logistics
    - pricing
    - customer spending
  understood_facts:
    - At Xiao Ye, Lin has struggled with similar logistics, in addition to price.
    - Selling burgers brings in new guests, but the amount of money each guest spends on burger night is significantly lower than a regular service.
    - The restaurant needs to feed many more guests in a night to make the same amount of money on burger nights, which changes the flow of service as they work to turn tables.
  questions_i_have:
    - What are the specific logistics challenges that Lin has faced at Xiao Ye?
    - How does the lower customer spending on burger nights impact the restaurant's revenue and operations?

=====
```

### AI Benchmark

`evaluate.py` can process an output file and run a benchmark rating each model for 20 different metrics. (readability,
coherence, grammer, etc). At the end of this "evaluation",
we also process a little graph to show the average performance of each model. You can use any model to run these
evaluations but it would be common sense to use the best models for this task.
(sonnet-3.7 / gemini-1.5-pro-002)

