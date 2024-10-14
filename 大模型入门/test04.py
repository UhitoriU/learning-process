import openai 
import os
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
BASE_URL = os.getenv("BASE_URL")
client = openai.OpenAI(api_key=OPENAI_API_KEY,base_url=BASE_URL)

def translate_text(text):
    content = f"请将以下中文文本翻译成英文:\n{text}"
    response = client.chat.completions.create(
        model="gpt-3.5-turbo", 
        messages=[{"role": "user", "content": content}]
    )
    translated_text = response.choices[0].message.content
    return translated_text

text_to_translate = "大家好，一起来参加DataWhale的《ChatGPT使用指南》组队学习课程吧！"
translated_text = translate_text(text_to_translate)
print("原始文本: ", text_to_translate)
print("输出文本: ", translated_text)

