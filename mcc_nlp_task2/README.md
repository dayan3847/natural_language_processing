# Maestría en Ciencias de la Computación - Universidad Autónoma de Yucatán

## Natural Language Processing

### Task2: Represent sentences as Vectors

#### Description

1. Representar las siguientes oraciones como vectores:
    * Somos héroes
    * Luis Pedro y Juan Luis son héroes

2. Identificar el Vocabulario (Dimensiones del vector):
    * Vocabulario: [Somos, héroes, son, Luis, Pedro, y, Juan]

3. Traducir el texto en vectores usando vocabulario como dimensiones y frecuencias de palabras como valores:
    * Somos héroes [1, 1, 0, 0, 0, 0, 0]
    * Luis Pedro y Juan Luis son héroes [0, 1, 1, 2, 1, 1, 1]

#### Code

```python
def get_vocabulary(sentences: list[str]) -> set[str]:
    return set(' '.join(sentences).split())


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
```

#### Output

```text
Vocabulary ['Juan', 'Luis', 'Pedro', 'Somos', 'héroes', 'son', 'y']
Somos héroes [0, 0, 0, 1, 1, 0, 0]
Luis Pedro y Juan Luis son héroes [1, 2, 1, 0, 1, 1, 1]
```