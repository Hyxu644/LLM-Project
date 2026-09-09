import json
import os
from typing import Sequence

from langchain_community.chat_models import ChatTongyi
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.messages import BaseMessage, message_to_dict, messages_from_dict
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnableWithMessageHistory

# message_to_dict: Single message object (BaseMessage instance) -> dict
# messages_from_dict: [dict, dict...] -> [message, message...]
# AIMessage, HumanMessage, and SystemMessage are all subclasses of BaseMessage


class FileChatMessageHistory(BaseChatMessageHistory):
    def __init__(self, session_id: str, storage_path: str):
        self.session_id = session_id  # Session ID
        self.storage_path = (
            storage_path  # Directory path storing history files for sessions
        )
        # Complete file path
        self.file_path = os.path.join(self.storage_path, self.session_id)

        # Ensure directory exists
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)

    def add_messages(self, messages: Sequence[BaseMessage]) -> None:
        # Sequence type (similar to list, tuple)
        all_messages = list(self.messages)  # Existing message list
        all_messages.extend(
            messages
        )  # Merge existing and new messages into a single list

        # Synchronously write data to local file
        # To avoid binary serialization issues, convert BaseMessage objects to dicts
        # and store them as a JSON string.
        # message_to_dict: BaseMessage instance -> dict
        # new_messages = []
        # for message in all_messages:
        #     d = message_to_dict(message)
        #     new_messages.append(d)

        new_messages = [message_to_dict(message) for message in all_messages]
        # Write data to file
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(new_messages, f)

    @property  # @property decorator allows accessing messages as an attribute
    def messages(self) -> list[BaseMessage]:
        # Inside file: list[dict]
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                messages_data = json.load(f)  # Returns list[dict]
                return messages_from_dict(messages_data)
        except FileNotFoundError:
            return []

    def clear(self) -> None:
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump([], f)


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


def get_history(session_id):
    return FileChatMessageHistory(session_id, "./chat_history")


# Create a new chain enhancing the base chain with persistent file history
conversation_chain = RunnableWithMessageHistory(
    base_chain,  # The base chain to enhance
    get_history,  # Function retrieving FileChatMessageHistory instance by session_id
    input_messages_key="input",  # Key corresponding to the user input placeholder
    history_messages_key="chat_history",  # Key corresponding to the chat history placeholder
)


if __name__ == "__main__":
    # Standard configuration specifying session_id for current execution
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