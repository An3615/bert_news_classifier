# 基于BERT模型的今日头条新闻文本分类系统

> 基于 BERT 的中文新闻文本分类系统，支持用户输入标题或内容自动预测新闻类别，并进行本地部署。

---

## 项目简介

本项目实现了一个完整的 **中文新闻文本分类系统**，包括：

- 使用python的request库爬取今日头条上的7大类新闻（如军事、财经等）数据，并贴上类别标签，保存到csv文件，用于模型训练
- 对标题与摘要进行文本清洗、分词处理
- 使用 `BERT` 模型对新闻进行多分类训练
- 模型部署于 FastAPI 后端，支持实时预测
- 使用 HTML+JavaScript 构建简洁前端

## 技术栈

| 类型       | 技术工具 |
|------------|----------|
| 编程语言   | Python 3.9+ |
| 深度学习   | PyTorch, Transformers |
| 模型部署   | FastAPI, Uvicorn |
| 前端交互   | HTML, JavaScript |
| 文本处理   | jieba, 正则表达式 |
| 其他工具   | joblib, pandas |

---

## 📁 项目结构

```
  bert_news_classifier/
  ├── app/
  │   ├── main.py           # FastAPI 后端主应用
  │   └── model/
  │       ├── bert_clf/     # 训练好的 BERT 模型
  │       └── label_encoder.pkl
  ├── static/
  │   └── index.html        # 前端页面
  ├── requirements.txt
  └── README.md
```
