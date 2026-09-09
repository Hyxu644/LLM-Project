from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

parser = StrOutputParser()
model = ChatTongyi(model="qwen3-max")
prompt = PromptTemplate.from_template(
    "My neighbor's last name is {lastname}, and they just had a {gender}. Please suggest a name, return only the name without any other text."
)

chain = prompt | model | parser | model | parser

res: str = chain.invoke({"lastname": "Smith", "gender": "daughter"})
print(res)
print(type(res))