from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import torch
from transformers import BertForSequenceClassification, BertTokenizer
import joblib
import os

app = FastAPI()
# 允许跨域请求
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 模型加载
model_path = os.path.join("app", "model", "bert_clf")
label_path = os.path.join("app", "model", "label_encoder.pkl")
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = BertForSequenceClassification.from_pretrained(model_path).to(device).eval()
tokenizer = BertTokenizer.from_pretrained(model_path)
label_encoder = joblib.load(label_path)

# 请求体
class TextRequest(BaseModel):
    text: str

# 路由
@app.post("/predict")
def predict(req: TextRequest):
    cleaned = req.text
    inputs = tokenizer(cleaned, truncation=True, padding='max_length', max_length=128, return_tensors="pt").to(device)
    with torch.no_grad():
        logits = model(**inputs).logits
        pred = torch.argmax(logits, dim=1).cpu().item()
        label = label_encoder.inverse_transform([pred])[0]
    return {"label": label}

# 提供前端页面
@app.get("/")
def read_index():
    return FileResponse("static/index.html")