```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Message(BaseModel):
    text: str

@app.get("/")
Paste:
def home():
    return {"message": "OrderFix AI is running"}

@app.post("/parse-order")
def parse_order(msg: Message):
    return {
        "input": msg.text,
        "output": "Structured order (demo only)"
    }
