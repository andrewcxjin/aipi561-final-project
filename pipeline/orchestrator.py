from .modules.trend_scraper import fetch_trends
from .modules.sentiment_analysis import analyze_sentiment
from .modules.report_generator import generate_report

def run_trend_pipeline():
    trends = fetch_trends()
    sentiment = analyze_sentiment(trends)
    return generate_report(trends, sentiment)