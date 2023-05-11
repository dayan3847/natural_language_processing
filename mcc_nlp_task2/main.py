# Get Vocabulary
def get_vocabulary(sentences: list[str]) -> set[str]:
    return set(' '.join(sentences).split())


def get_vocabulary2(sentences: list[str]) -> set[str]:
    vocabulary: set[str] = set()
    for sentence in sentences:
        for word in sentence.split():
            vocabulary.add(word)
    return vocabulary


def get_vocabulary_ordered(sentences: list[str]) -> list[str]:
    return sorted(list(get_vocabulary(sentences)))


def get_vectors(sentences: list[str], vocabulary: list[str]) -> dict[str, list[int]]:
    vectors: dict[str, list[int]] = {}
    for sentence in sentences:
        vector: list[int] = []
        for word in vocabulary:
            count: int = sentence.count(word)
            vector.append(count)
        vectors[sentence] = vector
    return vectors


# Example
def example():
    sentences: list[str] = [
        'Somos héroes',
        'Luis Pedro y Juan Luis son héroes'
    ]

    vocabulary: list[str] = get_vocabulary_ordered(sentences)
    print('Vocabulary', vocabulary)

    vectors = get_vectors(sentences, vocabulary)
    for v in vectors:
        print(v, vectors[v])


if __name__ == '__main__':
    example()
