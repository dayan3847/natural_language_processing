import numpy as np
import networkx as nx
from matplotlib import pyplot as plt


class Tools:
    @staticmethod
    def draw(graph: nx.Graph):
        nx.draw(
            graph,
            with_labels=True,
            font_weight='bold',
            node_size=1000,
            node_color='green',
        )
        plt.show()

    @staticmethod
    def suma_palablas(palabras, emb):
        result = np.zeros(300)
        for p in palabras:
            if p not in emb:
                continue
            v = emb[p]
            result = result + v
        return result

    @staticmethod
    def convert_to_dict(btc) -> dict:
        result = {}
        for b in btc:
            result[b[0]] = b[1]
        return result

    @staticmethod
    def precision(word_input: str, btc, k: int = 1) -> int:
        count = min(k, len(btc))
        for i in range(count):
            b = list(btc.keys())[i]
            if b == word_input:
                return 1
        return 0
