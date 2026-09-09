from langchain_community.llms.tongyi import Tongyi
from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate

# Template for examples
example_template = PromptTemplate.from_template("Word: {word}, Antonym: {antonym}")

# Example data injection; must be a list containing dictionaries
examples_data = [
    {"word": "big", "antonym": "small"},
    {"word": "up", "antonym": "down"},
]

few_shot_template = FewShotPromptTemplate(
    example_prompt=example_template,  # Template for example data
    examples=examples_data,  # Example data used for dynamic injection
    prefix="Tell me the antonym of the word. Here are some examples:",  # Prompt prefix before examples
    suffix="Based on the examples above, what is the antonym of {input_word}?",  # Prompt suffix after examples
    input_variables=[
        "input_word"
    ],  # Variable names required in the prefix or suffix
)

prompt_text = few_shot_template.invoke(input={"input_word": "left"}).to_string()
print(prompt_text)

model = Tongyi(model="qwen-max")

print(model.invoke(input=prompt_text))