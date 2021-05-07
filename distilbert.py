import json
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer

with open('config.json') as file:
    config = json.load(file)

model_path = config['MODEL_PATH']
model = SentenceTransformer(f'{model_path}distilbert-base-nli-stsb-mean-tokens/')
app = FastAPI()

class Sentence(BaseModel):
    text: str

class Embedding(BaseModel):
    values: list

@app.post("/vectorizer/api/v0.1/distilbert/", response_model=Embedding)
async def vectorize(sentence : Sentence):
    values = model.encode(sentence.text)
    emb = {'values' : values.tolist()}
    return emb