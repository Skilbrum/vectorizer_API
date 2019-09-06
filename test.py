import random_text
import pandas as pd
import requests

corpus=random_text.generate_corpus(corpus_len=1000,
                                   min_text_len=20,
                                   max_text_len=100,
                                   dict_len=5000,
                                   min_word_len=2,
                                   max_word_len=8)
corpus=pd.Series(corpus)

req=requests.post(url='http://localhost:5000/vectorizer/api/v0.1/tfidf', json=corpus.to_json())
X=pd.DataFrame(req.json())

assert X.shape[0]==corpus.shape[0]
assert (X.dtypes==float).all()

print('ok')