import requests
import nltk
from bs4 import BeautifulSoup
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from nltk.sentiment import SentimentIntensityAnalyzer
from deep_translator import GoogleTranslator
import gtts
import os



nltk.download('vader_lexicon')

NEWS_API_KEY = "7e72763bebb54fd79cb632390738cbb1"
NEWS_API_URL = "https://newsapi.org/v2/everything"

# Function to fetch news articles
def fetch_news(company):
    params = {
        "q": company,
        "apiKey": NEWS_API_KEY,
        "language": "en",
        "sortBy": "relevancy",
        "pageSize": 10
    }
    response = requests.get(NEWS_API_URL, params=params)
    data = response.json()

    articles = []
    if "articles" in data:
        for item in data["articles"]:
            full_text = scrape_article_text(item["url"])
            summary = summarize_text(full_text) if full_text else "No summary available."
            articles.append({
                "title": item["title"],
                "summary": summary,
                "link": item["url"],
                "published_at": item["publishedAt"],
                "source": item["source"]["name"]
            })
    return articles

# Function to scrape full article text
def scrape_article_text(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        paragraphs = soup.find_all("p")
        full_text = " ".join([p.text for p in paragraphs])
        return full_text
    except Exception:
        return ""

# Function to summarize text
def summarize_text(text, sentences_count=3):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentences_count)
    return " ".join([str(sentence) for sentence in summary])

# Function for sentiment analysis
def analyze_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    score = sia.polarity_scores(text)
    if score['compound'] > 0.05:
        return "Positive"
    elif score['compound'] < -0.05:
        return "Negative"
    else:
        return "Neutral"

# Function to translate text to Hindi
def translate_to_hindi(text):
    return GoogleTranslator(source='en', target='hi').translate(text)

# Function to convert **headlines only** to speech
def text_to_speech(text, filename="news_headline.mp3"):
    if not text.strip():
        return None
    hindi_text = translate_to_hindi(text)
    tts = gtts.gTTS(text=hindi_text, lang='hi')
    tts.save(filename)
    return filename
