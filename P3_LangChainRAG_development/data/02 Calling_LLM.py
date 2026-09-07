from langchain_community.llms.tongyi import Tongyi

model = Tongyi(model="qwen-max")

# Get streaming output using the stream method
res = model.stream(input="Who are you and what can you do?")

for chunk in res:
    print(chunk, end="", flush=True)