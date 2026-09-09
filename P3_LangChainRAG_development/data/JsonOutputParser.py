from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.output_parsers import JsonOutputParser, StrOutputParser
from langchain_core.prompts import PromptTemplate

# Create the required parsers
str_parser = StrOutputParser()
json_parser = JsonOutputParser()

# Create the model instance
model = ChatTongyi(model="qwen3-max")

# First prompt template
first_prompt = PromptTemplate.from_template(
    "My neighbor's last name is {lastname}, and they just had a {gender}. Please help come up with a name "
    "and return it wrapped in JSON format. Require the key to be 'name' and the value to be the name you came up with. Please strictly follow the format requirements."
)

# Second prompt template
second_prompt = PromptTemplate.from_template(
    "Name: {name}, please help analyze its meaning."
)

# Construct the chain    (e.g., AIMessage('{"name": "Alice"}'))
chain = first_prompt | model | json_parser | second_prompt | model | str_parser

for chunk in chain.stream({"lastname": "Smith", "gender": "daughter"}):
    print(chunk, end="", flush=True)