# Maestría en Ciencias de la Computación - Universidad Autónoma de Yucatán

## Natural Language Processing

### Task3: Investigation of NLTK functionalities

#### Description

Research about 2 features available in NLTK.

#### Response:

##### 1. Named Entities:

Extracts named entities from a text.

###### Code

```python
from nltk import word_tokenize, pos_tag, ne_chunk


# Recognition of named entities
def named_entities(text: str):
    # POS Tokenization and Labeling
    tokens = word_tokenize(text)
    pos_tags = pos_tag(tokens)

    # Extraction of named entities
    named_entities = ne_chunk(pos_tags)

    print(f'Text: {text}')
    # Print named entities
    for entity in named_entities:
        if hasattr(entity, 'label'):
            print(entity.label() + ':', ' '.join(c[0] for c in entity))


if __name__ == '__main__':
    text1 = 'My name is John. I work at Google.'
    text2 = 'I am Jorge Carlos. I am a professor at UADY.'

    named_entities(text1)
    named_entities(text2)
```

###### Output

```text
Text: My name is John. I work at Google.
PERSON: John
ORGANIZATION: Google
Text: I am Jorge Carlos. I am a professor at UADY.
PERSON: Jorge Carlos
ORGANIZATION: UADY
```

##### 2. Sentiment Analysis:

Sentiment analysis is a natural language processing technique used to determine whether data is positive, negative or neutral.

###### Code

```python
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
```

###### Output

```text
Text: I love you!
Sentiment: {'neg': 0.0, 'neu': 0.182, 'pos': 0.818, 'compound': 0.6696}
Text: Hate you!
Sentiment: {'neg': 0.8, 'neu': 0.2, 'pos': 0.0, 'compound': -0.6114}
```
