from nltk.sentiment import SentimentIntensityAnalyzer


def analyze_sentiment(text: str):
    # Sentiment Analysis
    sentiment_analyzer = SentimentIntensityAnalyzer()

    sentiment = sentiment_analyzer.polarity_scores(text)
    print(f'Text: {text}')
    print(f'Sentiment: {sentiment}')


if __name__ == '__main__':
    positive_sentiment_sample_text = "I love you!"
    negative_sentiment_sample_text = "Hate you!"

    analyze_sentiment(positive_sentiment_sample_text)
    analyze_sentiment(negative_sentiment_sample_text)
