import networkx as nx
from typing import List

from src.graphs.GraphReducer import GraphReducer
from src.graphs.Precision import Precision
from src.tools.Tools import Tools


class PrecisionVectorSimilarityAndBetweennessCentrality(Precision):

    def estimate_input(self, t: str, subset: List[str]) -> dict:
        # Vector Similarity
        emb = self.data_set.import_emb()[t]
        sum_frequency = Tools.suma_palablas(subset, emb)
        btc = emb.most_similar([sum_frequency], topn=20)
        result_vector_similarity = Tools.convert_to_dict(btc)

        for w in subset:
            if w in result_vector_similarity:
                result_vector_similarity.pop(w)

        # Betweenness Centrality

        result_betweenness_centrality = {}

        graph = self.data_set.import_graphs()[t]
        sub_graph = GraphReducer.reduce_graph(graph, subset)
        result_betweenness_centrality = nx.betweenness_centrality(sub_graph, normalized=True, weight="weight")
        for w in subset:
            if w in result_betweenness_centrality:
                result_betweenness_centrality.pop(w)

        # sumar los dos diccionarios
        result = dict(result_vector_similarity)
        for w in result_betweenness_centrality:
            if w in result:
                result[w] *= result_betweenness_centrality[w]
            else:
                result[w] = result_betweenness_centrality[w]

        # ordenar
        result = dict(sorted(result.items(), key=lambda item: item[1], reverse=True))
        return result
