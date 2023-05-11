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
