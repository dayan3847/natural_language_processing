import nltk
import networkx as nx
from typing import List
from matplotlib import pyplot as plt
from networkx import Graph
from nltk.corpus import wordnet
from nltk.corpus.reader.wordnet import Synset
import scipy as sp


class WordnetTest:

    @staticmethod
    def download_nltk_data():
        nltk.download('wordnet')
        nltk.download('omw-1.4')

    def __init__(self, file_name: str):
        self.file_name: str = file_name
        self.graph: Graph = nx.Graph()

    def run(self):
        with open(self.file_name, 'r') as file:
            for line in file:
                # Dividir la línea en palabras
                words = line.strip().split()
                for word in words:
                    # verificar si es un sustantivo
                    if not wordnet.synsets(word, pos=wordnet.NOUN):
                        continue
                    # Buscar synset (conjunto de sinónimos) de la palabra
                    synsets: List[Synset] = wordnet.synsets(word)
                    for synset in synsets:
                        # Imprimir hiperónimos y hipónimos de cada synset
                        hypernyms: List[Synset] = synset.hypernyms()
                        for hypernym in hypernyms:
                            for lemma in hypernym.lemma_names():
                                self.graph.add_edge(lemma, word)
                        hyponyms: List[Synset] = synset.hyponyms()
                        for hyponym in hyponyms:
                            for lemma in hyponym.lemma_names():
                                self.graph.add_edge(word, lemma)

    # graficar el arbol
    def plot_tree(self):
        # create directed graph
        plt.figure(figsize=(10, 10))
        nx.draw(
            self.graph,
            with_labels=True,
            node_color='skyblue',
            node_size=1500,
            edge_cmap=plt.cm.Blues,
            font_size=8,
        )
        plt.show()

    def get_degree_centrality(self):
        degree_centrality = nx.degree_centrality(self.graph)
        sorted(degree_centrality.items(), key=lambda x: x[1], reverse=True)
        return degree_centrality


if __name__ == '__main__':
    file_name: str = 'squirrel.txt'
    # file_name: str = 'test2.txt'
    wordnet_test = WordnetTest(file_name)
    wordnet_test.run()
    degree_centrality = wordnet_test.get_degree_centrality()
    print(degree_centrality)
    # wordnet_test.plot_tree()

    {'metric_linear_unit': 0.0011331444759206798, 'a': 0.008498583569405098}
