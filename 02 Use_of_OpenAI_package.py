from openai import OpenAI
# Get client object
client = OpenAI(
    base_url="https://ws-w1kvgfyelontkfmk.cn-beijing.maas.aliyuncs.com/compatible-mode/v1"
)

# Call the model
response = client.chat.completions.create(
    model="qwen3-max",
    messages=[
        {"role": "system", "content": "You're a Python expert, and you say a lot."},
        {"role": "assistant", "content": "OK"},
        {"role": "user", "content": "print out the numbers from 1 to 10, use python"}
    ],
    stream=True  # Enable streaming output
)

# 3. Process results
# print(response.choices[0].message.content)
for chunk in response:
    print(
        chunk.choices[0].delta.content,
        end=" ",  # Separate each chunk with a space
        flush=True  # Flush the buffer immediately
    )