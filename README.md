__1. Configure__  
Set "MODEL_PATH" to distilbert-base-nli-stsb-mean-tokens directory in config.json__

__2. Run server:__  
```uvicorn --host 0.0.0.0 --port 5000 distilbert:app --reload```