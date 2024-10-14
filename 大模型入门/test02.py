from openai import OpenAI
import os
import numpy as np
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
BASE_URL = os.getenv("BASE_URL")
client = OpenAI(api_key=OPENAI_API_KEY,base_url=BASE_URL)
content = "请告诉我下面三句话的相似程度：\n1. 我喜欢你。\n2. 我钟意你。\n3.我不喜欢你。\n"
response = client.chat.completions.create(
    model="gpt-3.5-turbo", 
    messages=[{"role": "user", "content": content}]
)

print(response.choices[0].message.content)

content = """请告诉我下面三句话的相似程度：
1. 我喜欢你。
2. 我钟意你。
3. 我不喜欢你。
第一句话用a表示，第二句话用b表示，第三句话用c表示。
请以json格式输出两两语义相似度。仅输出json，不要输出其他任何内容。
"""
response = client.chat.completions.create(
    model="gpt-3.5-turbo", 
    messages=[{"role": "user", "content": content}],
)
print(response.choices[0].message.content)

