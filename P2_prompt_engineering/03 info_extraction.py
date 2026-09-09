import json
from openai import OpenAI

client = OpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

schema = ["Date", "Stock Name", "Opening Price", "Closing Price", "Trading Volume"]
examples_data = [  # Example data
    {
        "content": "2023-01-10, the stock market fluctuated. Qiangda Tech A-Share opened at 100 RMB today, once surged to 105 RMB, then fell back to 98 RMB, and finally closed at 102 RMB, with a trading volume of 520,000.",
        "answers": {
            "Date": "2023-01-10",
            "Stock Name": "Qiangda Tech A-Share",
            "Opening Price": "100 RMB",
            "Closing Price": "102 RMB",
            "Trading Volume": "520000",
        },
    },
    {
        "content": "2024-05-16, positive market news. NVIDIA US Stock opened at 105 USD today, once surged to 109 USD, then fell back to 100 USD, and finally closed at 116 USD, with a trading volume of 3,560,000.",
        "answers": {
            "Date": "2024-05-16",
            "Stock Name": "NVIDIA US Stock",
            "Opening Price": "105 USD",
            "Closing Price": "116 USD",
            "Trading Volume": "3560000",
        },
    },
]
questions = [  # Target questions
    "2025-06-16, positive market news. Chuanzhi Education A-Share opened at 66 RMB today, once surged to 70 RMB, then fell back to 65 RMB, and finally closed at 68 RMB, with a trading volume of 123,000.",
    "2025-06-06, positive market news. Heima Programmer A-Share opened at 200 RMB today, once surged to 211 RMB, then fell back to 201 RMB, and finally closed at 206 RMB.",
]

"""
[
    {"role": "system",      "content": f"Help me extract information. I will provide sentences, and you extract {schema} information, outputting as a JSON string. If certain information is missing, represent it as 'Not mentioned in text'. Refer to the following examples:"},

    {"role": "user",        "content": "2023-01-10, the stock market fluctuated. Qiangda Tech A-Share opened at 100 RMB today, once surged to 105 RMB, then fell back to 98 RMB, and finally closed at 102 RMB, with a trading volume of 520,000."},
    {"role": "assistant",   "content": '{"Date":"2023-01-10","Stock Name":"Qiangda Tech A-Share","Opening Price":"100 RMB","Closing Price":"102 RMB","Trading Volume":"520000"}'},
    {"role": "user",        "content": "2024-05-16, positive market news. NVIDIA US Stock opened at 105 USD today, once surged to 109 USD, then fell back to 100 USD, and finally closed at 116 USD, with a trading volume of 3,560,000."},
    {"role": "assistant",   "content": '{"Date":"2024-05-16","Stock Name":"NVIDIA US Stock","Opening Price":"105 USD","Closing Price":"116 USD","Trading Volume":"3560000"}'},

    {"role": "user",        "content": f"Following the examples above, extract information from this sentence: {sentence_text_to_extract}"}
]
"""

messages = [
    {
        "role": "system",
        "content": f"Help me extract information. I will provide sentences, and you extract {schema} information, outputting as a JSON string. If certain information is missing, represent it as 'Not mentioned in text'. Refer to the following examples:",
    }
]

for example in examples_data:
    messages.append({"role": "user", "content": example["content"]})
    messages.append(
        {
            "role": "assistant",
            "content": json.dumps(example["answers"]),
        }
    )

for q in questions:
    response = client.chat.completions.create(
        model="qwen3-max",
        messages=messages
                 + [
                     {
                         "role": "user",
                         "content": f"Following the examples above, extract information from this sentence: {q}",
                     }
                 ],
    )

    print(response.choices[0].message.content)