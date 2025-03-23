import nltk
nltk.download('punkt')




import streamlit as st
from api import get_news, NewsRequest
from utils import text_to_speech
import time
import base64




# Function to play audio automatically
def autoplay_audio(file_path):
    with open(file_path, "rb") as audio_file:
        audio_bytes = audio_file.read()
    b64 = base64.b64encode(audio_bytes).decode()
    audio_tag = f"""
        <audio autoplay>
        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
    """
    st.markdown(audio_tag, unsafe_allow_html=True)

# UI Function
def main():
    st.set_page_config(page_title="News Sentiment & Summarization", layout="wide")

    # Sidebar
    st.sidebar.markdown(
        "<h1 style='color:#00FFAF; text-align:center;'>📰 News Finder</h1>", 
        unsafe_allow_html=True
    )
    st.sidebar.write("Enter a company name below to get the latest summarized news with sentiment analysis:")

    company_name = st.sidebar.text_input("🔎 Company Name:")
    fetch_button = st.sidebar.button("Fetch News")

    st.sidebar.markdown("---")
    sentiment_summary_placeholder = st.sidebar.empty()

    st.markdown(
        "<h1 style='text-align:center; color:#00FFAF;'>📢 News Sentiment & Summarization</h1>",
        unsafe_allow_html=True
    )

    if fetch_button and company_name:
        response = get_news(NewsRequest(company=company_name))
        articles = response["articles"]

        if not articles:
            st.warning("No news found for this company.")
            return

        # Calculate sentiment summary
        sentiments = [article['sentiment'] for article in articles]
        positive = sentiments.count("Positive")
        negative = sentiments.count("Negative")
        neutral = sentiments.count("Neutral")

        sentiment_summary_placeholder.markdown(f"""
            <div style='padding:10px; background-color:#222; border-radius:10px; color:white; text-align:center;'>
                <h3>📊 Sentiment Summary</h3>
                <p>✅ Positive: <b style="color:lightgreen;">{positive}</b></p>
                <p>⚠️ Neutral: <b style="color:orange;">{neutral}</b></p>
                <p>❌ Negative: <b style="color:#FF4B4B;">{negative}</b></p>
            </div>
        """, unsafe_allow_html=True)

        # all_headlines = ". ".join([article['title'] for article in articles])
        # audio_file = text_to_speech(all_headlines)
        # if audio_file:
        #     autoplay_audio(audio_file)
        # Generate numbered headlines for audio
        all_headlines = ". ".join([f"{idx + 1}. {article['title']}" for idx, article in enumerate(articles)])
        audio_file = text_to_speech(all_headlines)
        if audio_file:
            autoplay_audio(audio_file)


        st.write("## Latest News Articles")

        for idx, article in enumerate(articles, start=1):
            sentiment_color = {
                "Positive": "#4CAF50",
                "Neutral": "#FFA500",
                "Negative": "#FF4B4B"
            }[article['sentiment']]

            st.markdown(f"""
                <div style='
                    border-radius: 12px; 
                    padding: 20px; 
                    margin-bottom: 20px; 
                    background: linear-gradient(145deg, #1f1f1f, #292929); 
                    box-shadow: rgba(0,0,0,0.4) 0px 5px 15px;
                    color: #f1f1f1; 
                '>
                    <h4 style="color:#00FFAF;">📰 {idx}. {article['title']}</h4>
                    <p><b>📝 Summary:</b> {article['summary']}</p>
                    <p><b>💡 Sentiment:</b> <span style="color:{sentiment_color}; font-weight:bold;">{article['sentiment']}</span></p>
                    <p><b>📅 Published At:</b> {article['published_at']}</p>
                    <a href="{article['link']}" target="_blank" style="color:#00FFAF; text-decoration:none;">🔗 Read Full Article</a>
                </div>
            """, unsafe_allow_html=True)
    elif not fetch_button:
        st.info("Enter a company name in the sidebar and click 'Fetch News' to begin.")

if __name__ == "__main__":
    main()
