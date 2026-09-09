from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_community.llms.tongyi import Tongyi
from langchain_core.prompts import (
    ChatPromptTemplate,
    FewShotPromptTemplate,
    PromptTemplate,
)

"""
PromptTemplate -> StringPromptTemplate -> BasePromptTemplate -> RunnableSerializable -> Runnable
FewShotPromptTemplate -> StringPromptTemplate -> BasePromptTemplate  -> RunnableSerializable -> Runnable
ChatPromptTemplate -> BaseChatPromptTemplate -> BasePromptTemplate  -> RunnableSerializable -> Runnable
Tongyi -> BaseLLM -> BaseLanguageModel -> RunnableSerializable -> Runnable
ChatTongyi -> BaseChatModel -> BaseLanguageModel -> RunnableSerializable -> Runnable
"""


template = PromptTemplate.from_template(
    "My neighbor is: {lastname}, favorite hobby: {hobby}"
)

res = template.format(lastname="John Doe", hobby="fishing")
print(res, type(res))


res2 = template.invoke({"lastname": "Jay Chou", "hobby": "singing"})
print(res2, type(res2))