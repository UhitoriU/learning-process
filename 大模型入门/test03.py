import pandas as pd
from openai import OpenAI
import os
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
BASE_URL = os.getenv("BASE_URL")
client = OpenAI(api_key=OPENAI_API_KEY,base_url=BASE_URL)
df = pd.read_csv("files/demo01.csv")
print(df.shape)
print(df.head())

def get_embedding(text,model = "text-embedding-ada-002"):
    emb_req = client.embeddings.create(model=model,input = text)
    return emb_req.data[0].embedding

import numpy as np
vec_base = []
for v in df.head().itertuples():
    emb = get_embedding(v.Questions)
    im = {
        "question": v.Questions,
        "embedding": emb,
        "answer": v.Link
    }
    vec_base.append(im)
query = "is kaggle alive?"
q_emb = get_embedding(query)
print(vec_base[1]["question"], vec_base[1]["answer"]) 
