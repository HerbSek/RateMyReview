# RateMyReview

**RateMyReview** is a FastAPI-powered service that uses **zero-shot text classification** to automatically assign ratings (1–5 stars) to customer reviews. Instead of relying on pre-labeled datasets, the system leverages Hugging Face’s `facebook/bart-large-mnli` model to classify reviews into custom labels such as *worst experience*, *bad experience*, *average experience*, *good experience*, and *excellent experience*.

### ✨ Features

* 🚀 **Zero-Shot Classification** – no manual dataset labeling required
* 📊 **Text-to-Rating Mapping** – converts review text into a numeric score (1–5)
* ⚡ **FastAPI Backend** – lightweight and production-ready API
* 🐳 **Dockerized** – ready to run in any containerized environment

### 🔧 Tech Stack

* [FastAPI](https://fastapi.tiangolo.com/) – API framework
* [Transformers](https://huggingface.co/transformers/) – NLP models
* [PyTorch](https://pytorch.org/) – deep learning backend
* [Docker](https://www.docker.com/) – containerization

### 📌 Example Usage

```json
Input:  
"This was the most disappointing purchase I've ever made."  

Output:  
{
  "score": 1,
  "label": "worst experience"
}
```

### 🚀 Getting Started

1. Clone the repo

   ```bash
   git clone https://github.com/<your-username>/RateMyReview.git
   cd RateMyReview
   ```

2. Build and run with Docker

   ```bash
   docker build -t ratemyreview .
   docker run -p 8000:8000 ratemyreview
   ```

3. Send a request

   ```bash
   curl -X POST "http://127.0.0.1:8000/" -H "Content-Type: application/json" -d '{"review": "Great product, I loved it!"}'
   ```

---

💡 This project demonstrates how **zero-shot learning** can be applied to real-world customer feedback analysis without a custom training dataset.
