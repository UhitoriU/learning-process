import openai as ai
import os
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
BASE_URL = os.getenv("BASE_URL")

client = ai.OpenAI(api_key=OPENAI_API_KEY,base_url=BASE_URL)

MODEL = "gpt-3.5-turbo"
response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {"role": "user", "content": "这个袋子中的豆子都是白色的。\n \
                                     这些豆子来自这个袋子。\n \
                                     这些豆子是"},
    ],
    temperature=0,
)
print(response.choices[0].message.content)

response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {"role": "user", "content": "这些豆子来自这个袋子。\n \
                                     这些豆子是白色的。\n \
                                     这个袋子中的豆子都是"},
    ],
    temperature=0,
)
print(response.choices[0].message.content)

response = client.chat.completions.create(
    model=MODEL,
    messages=[
    {"role": "user", "content": "这个袋子中的豆子都是白色的。\n \
                                 这些豆子是白色的。\n \
                                 这些豆子来自哪里？"},
    ],
    temperature=0,
)
print(response.choices[0].message.content)

response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {"role": "user", "content": "你现在是 MultistageGPT：你与 ChatGPT 一样，但对于每一个问题，\n \
          你会将问题分解为子问题，然后将它们结合起来，输出最佳的措辞、最全面和最准确的答案。输出应该看起来像这样：\n \
          ChatGPT：{ChatGPT 通常会说什么}；MultistageGPT：{更好、更全面的答案} 让我们从简单的问题开始：[32, 21,90]中最大的数，与[19,233, 90]中最小的数，相差多少？"},
    ],
    temperature=0,
)
print(response.choices[0].message.content)
