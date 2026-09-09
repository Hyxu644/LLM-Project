from openai import OpenAI

# 1. Get client object, OpenAI class instance
client = OpenAI(
    base_url="https://ws-w1kvgfyelontkfmk.cn-beijing.maas.aliyuncs.com/compatible-mode/v1"
)

examples_data = {  # Example data
    'News Report': 'Today, the stock market experienced a round of volatility, influenced by macroeconomic data and global trade tensions. Investors are closely watching possible policy adjustments by the Federal Reserve to adapt to market uncertainty.',
    'Financial Report': "The company's annual financial report shows steady earnings growth last year, accompanied by a strong balance sheet. A stable economic environment and effective management execution laid the foundation for healthy corporate growth.",
    'Company Announcement': 'The company is pleased to announce the successful completion of its latest M&A transaction, acquiring a leading firm in the artificial intelligence sector. This strategic move will expand our business domains and enhance market competitiveness.',
    'Analyst Report': 'The latest industry analysis report indicates that tech innovation will be the primary driver of future growth. Cloud computing, AI, and digital transformation are key factors leading industry development, and investors should pay attention to these trends.'
}

# Category list
examples_types = ['News Report', 'Financial Report', 'Company Announcement', 'Analyst Report']

# Questions data
questions = [
    "Today, the central bank issued an announcement declaring an interest rate cut to stimulate economic growth. This rate cut will affect lending rates and impact financial markets over the coming quarters.",
    "ABC Company announced today that it has successfully completed the acquisition of XYZ Company's equity. This transaction is a key initiative for ABC Company to expand its scope of operations and strengthen market competitiveness. Reports indicate this acquisition will consolidate ABC's industry standing and open broader avenues for future business growth. For details, please refer to the official company website announcement board.",
    "The company balance sheet demonstrates robust debt-servicing capability and ample cash flow, laying a solid financial foundation for future investment and expansion.",
    "The latest analytical report points out that the renewable energy industry is expected to sustain growth in the coming years; investors should monitor investment opportunities in this field.",
    "Xiao Ming likes Shin-chan!"
]

"""
[
    {"role": "system",      "content": "You are a financial expert. Classify the text into ['News Report', 'Financial Report', 'Company Announcement', 'Analyst Report']. If unclear, classify it as 'Unclear Category'. Examples are below:"},

    {"role": "user",        "content": "Today, the central bank issued an announcement declaring..."},
    {"role": "assistant",   "content": "News Report"},
    {"role": "user",        "content": "ABC Company announced today that it has successfully completed..."},
    {"role": "assistant",   "content": "Company Announcement"},
    {"role": "user",        "content": "The company balance sheet demonstrates robust debt-servicing..."},
    {"role": "assistant",   "content": "Financial Report"},
    {"role": "user",        "content": "The latest analytical report points out that renewable energy..."},
    {"role": "assistant",   "content": "Analyst Report"},

    {"role": "user",        "content": "Question text here"}
]
"""

messages = [
    {"role": "system",
     "content": "You are a financial expert. Classify the text into ['News Report', 'Financial Report', 'Company Announcement', 'Analyst Report']. If unclear, classify it as 'Unclear Category'. Examples are below:"},
]

for key, value in examples_data.items():
    messages.append({"role": "user", "content": value})
    messages.append({"role": "assistant", "content": key})

# Query the model
for q in questions:
    response = client.chat.completions.create(
        model="qwen3-max",
        messages=messages + [
            {"role": "user", "content": f"Following the examples, output the category for this text: {q}"}]
    )

    print(response.choices[0].message.content)