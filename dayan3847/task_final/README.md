# Universidad Autónoma de Yucatán

## Facultad de Matemáticas

### Natural Language Processing

**Teacher:** Dr. Jorge Carlos Reyes

**Student:** Dayan Bravo Fraga

# GitHub Repository

All tasks are in the repository:

https://github.com/dayan3847/natural_language_processing

# BERT

Bidirectional Encoder Representations from Transformers

## Colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/dayan3847/natural_language_processing/blob/master/dayan3847/task_final/spam_detection_bert.ipynb)

# Doc2vec

### ¿Qué es Doc2vec?

Doc2vec es una técnica de procesamiento de lenguaje natural que se basa en Word2vec y se utiliza para crear
representaciones numéricas de documentos. Como sabes, las palabras mantienen una estructura lógica (gramatical), pero
los documentos no tienen ninguna estructura lógica. Para resolver este problema, se necesita agregar otro vector (ID de
párrafo) con el modelo Word2vec.

### Aplicaciones

Doc2vec se utiliza en una variedad de aplicaciones de procesamiento de lenguaje natural, como la clasificación de
documentos, la agrupación de documentos y la recuperación de información

### Clasificación

Doc2vec se puede utilizar para la clasificación de documentos. En este caso, se entrena un modelo Doc2vec en un conjunto
de documentos etiquetados y se utiliza para asignar una etiqueta a un nuevo documento

## Colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/dayan3847/natural_language_processing/blob/master/dayan3847/task_final/spam_detection_doc2vec.ipynb)

## Referencias

- https://arxiv.org/abs/1405.4053 (Doc2vec, Quoc V. Le, Tomas Mikolov, 2014)
- https://thinkinfi.com/simple-doc2vec-explained/
- https://radimrehurek.com/gensim/auto_examples/tutorials/run_doc2vec_lee.html
- https://radimrehurek.com/gensim/models/doc2vec.html
- https://medium.com/red-buffer/doc2vec-computing-similarity-between-the-documents-47daf6c828cd
- https://medium.com/@klintcho/doc2vec-tutorial-using-gensim-ab3ac03d3a1
- https://itelligent.es/es/pln-clasificacion-automatica-documentos/
- https://web.archive.org/web/20151231073758/http://deeplearning4j.org/doc2vec.html