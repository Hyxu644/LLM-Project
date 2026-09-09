# from langchain_community.chat_models.tongyi import ChatTongyi
# from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
#
# # Get the model object; qwen3-max is a chat model
# model = ChatTongyi(model="qwen3-max")
#
# # Prepare the list of messages
# messages = [
#     SystemMessage(content="You are a frontier poet."),
#     HumanMessage(content="Write a Tang poem."),
#     AIMessage(
#         content="Hoeing weeds under the midday sun, sweat drips into the soil below. Who knows that on the plate, every single grain comes from hard toil?"
#     ),
#     HumanMessage(
#         content="Following the format of your previous reply, write another Tang poem."
#     ),
# ]
#
# # Call stream for streaming execution
# res = model.stream(input=messages)
#
# # Iterate through the for loop to print output, accessing the text content via .content
# for chunk in res:
#     print(chunk.content, end="", flush=True)

from langchain_community.chat_models.tongyi import ChatTongyi

# Get the model object; qwen3-max is a chat model
model = ChatTongyi(model="qwen3-max")

# Prepare the list of messages
messages = [
    # (role, content) roles: system/human/ai
    ("system", "You are a frontier poet."),
    ("human", "Write a Tang poem."),
    (
        "ai",
        "Hoeing weeds under the midday sun, sweat drips into the soil below. Who knows that on the plate, every single grain comes from hard toil.",
    ),
    (
        "human",
        "Following the format of your previous reply, write another Tang poem.",
    ),
]

# Call stream for streaming execution
res = model.stream(input=messages)

# Iterate through the for loop to print output, accessing the text content via .content
for chunk in res:
    print(chunk.content, end="", flush=True)