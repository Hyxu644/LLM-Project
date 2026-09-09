from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

chat_prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a frontier poet who can compose poetry."),
        MessagesPlaceholder("history"),
        ("human", "Please write another Tang poem."),
    ]
)

history_data = [
    ("human", "Write a Tang poem."),
    (
        "ai",
        "Before my bed, the moonlight shines bright, looking like frost upon the ground. Raising my head, I gaze at the bright moon; lowering my head, I long for my home.",
    ),
    ("human", "Great poem, write another one."),
    (
        "ai",
        "Hoeing weeds under the midday sun, sweat drips into the soil below. Who knows that on the plate, every single grain comes from hard toil?",
    ),
]

# StringPromptValue    to_string()
prompt_text = chat_prompt_template.invoke({"history": history_data}).to_string()

model = ChatTongyi(model="qwen3-max")

res = model.invoke(prompt_text)

print(res.content, type(res))