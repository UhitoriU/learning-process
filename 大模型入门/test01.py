from openai import OpenAI
import os
import numpy as np
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
BASE_URL = os.getenv("BASE_URL")
client = OpenAI(api_key=OPENAI_API_KEY,base_url=BASE_URL)
text = "我喜欢你"
model = "text-embedding-ada-002"
emb_req = client.embeddings.create(input=[text], model=model)
emb = emb_req.data[0].embedding
print(len(emb),end=',')
print(type(emb)) 

def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2)/(np.linalg.norm(vec1) * np.linalg.norm(vec2))
def get_embedding(text,model = "text-embedding-ada-002"):
    emb_req = client.embeddings.create(model=model,input = text)
    return emb_req.data[0].embedding
text1 = "我喜欢你"
text2 = "我钟意你"
text3 = "我不喜欢你"
emb1 = get_embedding(text1, "text-embedding-3-large")
emb2 = get_embedding(text2, "text-embedding-3-large")
emb3 = get_embedding(text3, "text-embedding-3-large")
print("{},{},{}".format(emb1,emb2,emb3))
print(cosine_similarity(emb1, emb2))
print(cosine_similarity(emb1, emb3))
print(cosine_similarity(emb2, emb3))

