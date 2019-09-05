from flask import Flask, request
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

api_doc="""
API for TFIDF vectorizer.
Use POST HTTP method with json of form {'textid1':'text1', 'textid2':'text2', ...}
Returns Dataframe-friendly json with index {'textid1', 'textid2', ...} and float values
"""

def tfidf_vectorize(series):
    df=TfidfVectorizer().fit_transform(series).todense()
    df=pd.DataFrame(df, index=series.index)
    return df

app = Flask(__name__)

@app.route('/vectorizer/api/v0.1/tfidf', methods=['GET', 'POST'])

def vectorize():
    if request.method=='POST':
        req = request.json
        req=pd.read_json(req, typ='series')
        resp=tfidf_vectorize(req)
        resp=resp.to_json()
        return resp
    else:
        return api_doc

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
