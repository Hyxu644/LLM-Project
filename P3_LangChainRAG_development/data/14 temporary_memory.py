from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    PromptTemplate,
)
from langchain_core.runnables.history import RunnableWithMessageHistory

model = ChatTongyi(model="qwen3-max")
# prompt = PromptTemplate.from_template(
#     "You need to respond to user questions based on conversation history. Conversation history: {chat_history}, User question: {input}, Please answer"
# )
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You need to respond to user questions based on the conversation history. Conversation history:",
        ),
        MessagesPlaceholder("chat_history"),
        ("human", "Please answer the following question: {input}"),
    ]
)

str_parser = StrOutputParser()


def print_prompt(full_prompt):
    print("=" * 20, full_prompt.to_string(), "=" * 20)
    return full_prompt


base_chain = prompt | print_prompt | model | str_parser


store = (
    {}
)  # Key is session_id, value is an instance of InMemoryChatMessageHistory
# Retrieve the InMemoryChatMessageHistory instance via session_id
def get_history(session_id):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()

    return store[session_id]


# Create a new chain wrapping the base chain to automatically attach message history
conversation_chain = RunnableWithMessageHistory(
    base_chain,  # The base chain to enhance
    get_history,  # Function to retrieve InMemoryChatMessageHistory object by session_id
    input_messages_key="input",  # Key corresponding to the user input placeholder in the prompt
    history_messages_key="chat_history",  # Key corresponding to the chat history placeholder in the prompt
)


if __name__ == "__main__":
    # Standard format: pass LangChain configuration specifying the session_id for the current run
    session_config = {"configurable": {"session_id": "user_001"}}

    # res = conversation_chain.invoke({"input": "Xiao Ming has 2 cats"}, session_config)
    # print("1st execution:", res)
    #
    # res = conversation_chain.invoke({"input": "Xiao Gang has 1 dog"}, session_config)
    # print("2nd execution:", res)

    res = conversation_chain.invoke(
        {"input": "How many total pets are there?"}, session_config
    )
    print("3rd execution:", res)