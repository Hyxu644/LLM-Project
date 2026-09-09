from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

model = ChatTongyi(model="qwen3-max")
str_parser = StrOutputParser()

first_prompt = PromptTemplate.from_template(
    "My neighbor's last name is {lastname}, and they just had a {gender}. Please help come up with a name. Generate only one name and return just the name, no extra information."
)

second_prompt = PromptTemplate.from_template(
    "Name: {name}, please help analyze its meaning."
)

# Function input parameter: AIMessage -> dict ({"name": "xxx"})
# my_func = RunnableLambda(lambda ai_msg: {"name": ai_msg.content})

chain = (
    first_prompt
    | model
    | (lambda ai_msg: {"name": ai_msg.content})
    | second_prompt
    | model
    | str_parser
)

for chunk in chain.stream({"lastname": "Cao", "gender": "girl"}):
    print(chunk, end="", flush=True)