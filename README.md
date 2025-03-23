---
title: News Sentiment Analyzer
emoji: 🐨
colorFrom: gray
colorTo: blue
sdk: streamlit
sdk_version: 1.43.2
app_file: app.py
pinned: false
short_description: 'simple app to analyze news sentiment '
---

# News Summarization & Sentiment Analysis

## Overview
This project is a web-based application that extracts news articles related to a given company, performs sentiment analysis, generates a comparative analysis, and converts the summarized content into Hindi speech.

## Features
- **News Extraction:** Fetches news articles using NewsAPI and scrapes additional content when available.
- **Sentiment Analysis:** Categorizes each article as Positive, Negative, or Neutral.
- **Comparative Analysis:** Provides an overview of sentiment distribution across articles.
- **Text-to-Speech:** Converts summarized news titles into Hindi speech.
- **Web Interface:** Allows users to input a company name via a Streamlit UI.
- **API Integration:** Backend developed using FastAPI to communicate with the frontend.

## Installation
### Prerequisites
Ensure you have Python installed (>= 3.8). Install the required dependencies:

```bash
pip install requests nltk beautifulsoup4 gtts deep-translator streamlit fastapi pydantic uvicorn
```

### Download NLTK Data
To enable sentiment analysis, run:
```python
import nltk
nltk.download('vader_lexicon')
```

## Usage
### Running the FastAPI Backend
Start the FastAPI server using:
```bash
uvicorn news:app --reload
```

### Running the Streamlit UI
Launch the web application:
```bash
streamlit run news.py
```

## API Endpoints
- `POST /get_news/`
  - **Request Body:**
    ```json
    { "company": "Tesla" }
    ```
  - **Response:**
    ```json
    {
      "articles": [...],
      "sentiment_summary": {"Positive": 3, "Negative": 4, "Neutral": 3}
    }
    ```

## Deployment
- **Deploy FastAPI Backend:** Use services like **AWS, Heroku, or Render**.
- **Deploy Streamlit UI:** Host on **Streamlit Cloud or Hugging Face Spaces**.

## Acknowledgments
- [NewsAPI](https://newsapi.org/) for fetching news.
- [NLTK](https://www.nltk.org/) for sentiment analysis.
- [Google Translate API](https://pypi.org/project/deep-translator/) for Hindi translation.
- [Streamlit](https://streamlit.io/) for the UI.
- [FastAPI](https://fastapi.tiangolo.com/) for backend API.


