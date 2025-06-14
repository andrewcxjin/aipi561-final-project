from textblob import TextBlob

def analyze_sentiment(trends):
    return [TextBlob(text).sentiment.polarity for text in trends]