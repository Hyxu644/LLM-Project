from langchain_community.llms.tongyi import Tongyi
from langchain_core.prompts import PromptTemplate

# zero-shot
prompt_template = PromptTemplate.from_template(
    "My neighbor's last name is {lastname}, and they just had a {gender}. Help me come up with a name, keep the answer concise."
)
model = Tongyi(model="qwen-max")

# Simply call the .format method to inject information
# prompt_text = prompt_template.format(lastname="Smith", gender="daughter")
#
# model = Tongyi(model="qwen-max")
# res = model.invoke(input=prompt_text)
# print(res)

chain = prompt_template | model

res = chain.invoke(input={"lastname": "Smith", "gender": "daughter"})
print(res)