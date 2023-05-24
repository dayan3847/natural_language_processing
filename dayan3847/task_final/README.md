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

## ¿Qué es Doc2vec?

Doc2vec es una técnica de procesamiento de lenguaje natural que se basa en Word2vec y se utiliza para crear
representaciones numéricas de documentos. 

## Arquitectura
Como sabes, las palabras mantienen una estructura lógica (gramatical), pero
los documentos no tienen ninguna estrutura lógica. Para solucionar este problema, se
necesita agregar otro vector (ID de párrafo) al modelo de Word2vec. Esta es la única diferencia entre
Word2vec y Doc2vec.

Al igual que Word2vec, existen dos variantes de Doc2vec disponibles:

- **Modelo de Memoria Distribuida de Vectores de Párrafo (PV-DM):** Este modelo es similar al modelo 
Continuous-Bag-of-Words (CBOW) de Word2vec, que intenta adivinar la palabra de salida (palabra objetivo) a partir de 
las palabras vecinas (palabras de contexto) con la adición de un ID de párrafo.
- **Modelo de Bolsa de Palabras Distribuida (PV-DBOW):** Este modelo es similar al modelo Skip-Gram de Word2vec, que 
adivina las palabras de contexto a partir de una palabra objetivo.

## Entrenamiento de los modelos

El proceso de entrenamiento de los modelos Doc2vec implica aprender a asociar los documentos con sus contextos o 
documentos vecinos. A medida que se ajustan los vectores durante el entrenamiento, las representaciones vectoriales 
de los documentos se vuelven más precisas y útiles para diversas tareas de procesamiento del lenguaje natural.

### Proceso de entrenamiento
- **Preparación de datos**: Cada documento se representa como una secuencia de palabras o tokens.
- **Construcción de vocabulario:** Cada palabra se asigna a un identificador numérico único.
- **Creación de instancias de entrenamiento:** Se crean instancias de entrenamiento para el modelo Doc2vec. 
Cada instancia se compone de un documento y un contexto.
- **Inicialización de vectores de palabras y documentos:** Cada vector tiene una dimensión fija y representa una posición 
en un espacio vectorial.
- **Entrenamiento del modelo:** Se entrena el modelo utilizando técnicas de aprendizaje automático, como redes neuronales. 
Durante el entrenamiento, los vectores de palabras y documentos se ajustan de manera iterativa para maximizar la 
coherencia entre los documentos y su contexto.
- **Generación de representaciones vectoriales:** Se obtienen las representaciones vectoriales de los documentos. 
Estos vectores capturan la información semántica y contextual de los documentos en el espacio vectorial.

## Aplicaciones

Doc2vec se utiliza en una variedad de aplicaciones de procesamiento de lenguaje natural (NLP) y el analisis de texto, 
como:
- **Clasificación de documentos:** Doc2vec se puede utilizar para asignar automáticamente etiquetas o categorías a 
documentos. Al capturar la similitud semántica entre los textos, permite entrenar modelos de clasificación que pueden 
asignar las etiquetas adecuadas a nuevos documentos.

- **Agrupación de documentos:** Doc2vec se puede aplicar en sistemas de búsqueda y recuperación de información. 
Los embeddings generados por Doc2vec ayudan a encontrar documentos relevantes basados en la similitud semántica, 
lo que mejora la precisión y relevancia de los resultados de búsqueda.

- **Recuperación de información:** Con Doc2vec, se pueden construir sistemas de búsqueda y recuperación de información 
más efectivos. Al utilizar los embeddings generados por Doc2vec, es posible representar los documentos en un espacio 
vectorial donde la proximidad entre los vectores refleja la similitud semántica entre los textos.
- **Clasificacion**

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