from openai import OpenAI

client = OpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

examples_data = {
    "Yes": [
        (
            "Company ABC released quarterly earnings showing profit growth.",
            "Earnings report discloses Company ABC's profits went up.",
        ),
        (
            "Company ITCAST released annual earnings showing significant profit growth.",
            "Earnings report discloses Company ITCAST became more profitable.",
        ),
    ],
    "No": [
        (
            "Gold prices fell and investors sold off.",
            "Foreign exchange market trading volume reached a new high.",
        ),
        (
            "Central bank cut interest rates to stimulate economic growth.",
            "Innovation in new energy technologies.",
        ),
    ],
}

questions = [
    (
        "Interest rates rose, affecting the real estate market.",
        "High interest rates have a certain impact on real estate.",
    ),
    (
        "Oil prices fell significantly, energy companies face challenges.",
        "The trend of future smart city construction is becoming increasingly obvious.",
    ),
    (
        "The stock market rallied today, investors are optimistic.",
        "The continuously rising market makes investors satisfied.",
    ),
]

"""
    {"role": "system",      "content": "Help me perform text matching. I will give you 2 sentences enclosed in [], and you judge whether they match, answering Yes or No. Please refer to the following examples:"},

    {"role": "user",        "content": "Sentence 1: [Company ABC released quarterly earnings showing profit growth.], Sentence 2: [Earnings report discloses Company ABC's profits went up.]"},
    {"role": "assistant",   "content": "Yes"},
    {"role": "user",        "content": "Sentence 1: [Company ITCAST released annual earnings showing significant profit growth.], Sentence 2: [Earnings report discloses Company ITCAST became more profitable.]"},
    {"role": "assistant",   "content": "Yes"},
    {"role": "user",        "content": "Sentence 1: [Gold prices fell and investors sold off.], Sentence 2: [Foreign exchange market trading volume reached a new high.]"},
    {"role": "assistant",   "content": "No"},
    {"role": "user",        "content": "Sentence 1: [Central bank cut interest rates to stimulate economic growth.], Sentence 2: [Innovation in new energy technologies.]"},
    {"role": "assistant",   "content": "No"}, 

    {"role": "user",        "content": "Following the examples above, answer for these 2 sentences. Sentence 1: [...], Sentence 2: [...]"}
"""

messages = [
    {
        "role": "system",
        "content": "Help me perform text matching. I will give you 2 sentences enclosed in [], and you judge whether they match, answering Yes or No. Please refer to the following examples:",
    },
]

for key, value in examples_data.items():
    for t in value:
        messages.append(
            {"role": "user", "content": f"Sentence 1: [{t[0]}], Sentence 2: [{t[1]}]"}
        )
        messages.append({"role": "assistant", "content": key})

for q in questions:
    response = client.chat.completions.create(
        model="qwen3-max",
        messages=messages
                 + [
                     {
                         "role": "user",
                         "content": f"Sentence 1: [{q[0]}], Sentence 2: [{q[1]}]",
                     }
                 ],
    )

    print(response.choices[0].message.content)