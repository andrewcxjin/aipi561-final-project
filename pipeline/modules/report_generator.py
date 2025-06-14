def generate_report(trends, sentiment):
    report = "\n".join([
        f"Trend: {trend} | Sentiment Score: {score:.2f}"
        for trend, score in zip(trends, sentiment)
    ])
    return f"Fashion Trend Report:\n{report}"