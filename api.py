<<<<<<< HEAD
from fastapi import FastAPI
from pydantic import BaseModel
from utils import fetch_news, analyze_sentiment

app = FastAPI()

class NewsRequest(BaseModel):
    company: str

@app.post("/get_news/")
def get_news(data: NewsRequest):
    news_articles = fetch_news(data.company)
    for article in news_articles:
        article["sentiment"] = analyze_sentiment(article["summary"])
    
    return {"articles": news_articles}
=======
from fastapi import FastAPI
from pydantic import BaseModel
from utils import fetch_news, analyze_sentiment

app = FastAPI()

class NewsRequest(BaseModel):
    company: str

@app.post("/get_news/")
def get_news(data: NewsRequest):
    news_articles = fetch_news(data.company)
    for article in news_articles:
        article["sentiment"] = analyze_sentiment(article["summary"])
    
    return {"articles": news_articles}
>>>>>>> 3812ee3 (first commit)
