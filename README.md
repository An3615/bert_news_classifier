# 基于BERT模型的今日头条新闻文本分类系统

> 基于 BERT 的中文新闻文本分类系统，支持用户输入标题或内容自动预测新闻类别，并进行本地部署。

---

## 项目简介

本项目实现了一个从数据爬取到模型本地部署的完整的 **中文新闻文本分类系统**，包括：

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
  │       ├── bert_clf/     # 训练好的 BERT 模型（空文件夹，模型太大无法上传）
  │       ├── BERT_train.ipynb    # 模型训练代码
  │       └── label_encoder.pkl   # 类别标签编码器
  ├── data/
  │   ├── clawer.py    # 爬虫程序（需要自己抓包）
  │   └── toutiao_news.zip   # 抓取的新闻数据
  ├── static/
  │   └── index.html        # 前端页面
  ├── requirements.txt     # 项目依赖
  └── README.md    # 项目介绍文件
```

## 模型效果与页面展示

1. BERT模型分类报告

![image](https://github.com/user-attachments/assets/535fe00c-6c7b-4f6a-84d8-ef33c5df8ab3)

2. BERT模型分类效果混淆矩阵

![image](https://github.com/user-attachments/assets/a03f40b3-e4e5-4c07-b510-f910149613ce)

3. 前端界面预览

![image](https://github.com/user-attachments/assets/ccd07614-a80b-4b4e-9fc5-d7dc872ec86b)

---


## 个人收获

通过本项目，我收获了从 **自然语言处理建模** 到 **前后端一体化部署** 的完整工程能力，具体包括：

### NLP 与模型应用

- 熟练掌握了 **BERT 模型在中文文本分类中的使用**，包括 Tokenizer 编码、模型预测和标签反编码。
- 理解并实现了 **文本清洗、分词（基于 jieba）和标准化处理流程**，提升模型泛化能力。
- 对利用 `transformers` 库完成模型加载、推理和结构封装有了系统性理解。

### 工程部署实践

- 使用 **FastAPI** 构建后端服务，具备构建简单 API 接口、处理请求体（Pydantic）、管理模型状态的能力。
- 熟悉了 **模型持久化**（如 `model.save_pretrained()` 和 `joblib.dump()`）与加载机制，便于线上部署和迁移。

### 前端交互与用户体验

- 使用 **原生 HTML + JS** 构建轻量前端，用户可在浏览器直接输入新闻文本并查看预测结果。

### 综合能力提升

- 培养了从 **模型构建 ➝ 接口设计 ➝ 前端交互 ➝ 项目打包部署** 的完整项目思维。
- 加强了对 **实际应用中模型调用性能与用户交互体验** 的综合考量。
- 项目过程中注重代码结构清晰与模块化设计，提升了代码可维护性与扩展性。

本项目不仅帮助我加深了对 NLP 模型的理解，也锻炼了我将 AI 技术落地为产品的能力。

---
