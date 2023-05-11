import networkx as nx
from typing import List

from src.graphs.GraphReducer import GraphReducer
from src.graphs.Precision import Precision
from src.tools.Tools import Tools


class PrecisionVectorSimilarityAndDegreeCentrality(Precision):

    def estimate_input(self, t: str, subset: List[str]) -> dict:
        # Vector Similarity
        emb = self.data_set.import_emb()[t]
        sum_frequency = Tools.suma_palablas(subset, emb)
        btc = emb.most_similar([sum_frequency], topn=20)
        result_vector_similarity = Tools.convert_to_dict(btc)

        for w in subset:
            if w in result_vector_similarity:
                result_vector_similarity.pop(w)

        # Degree Centrality

        result_degree_centrality = {}
        graph = self.data_set.import_graphs()[t]
        sub_graph = GraphReducer.reduce_graph(graph, subset)
        if len(sub_graph.nodes()) == 0:
            return result_vector_similarity
        try:
            result_degree_centrality = nx.degree_centrality(sub_graph)
        except:
            return result_vector_similarity

        for w in subset:
            if w in result_degree_centrality:
                result_degree_centrality.pop(w)

        # sumar los dos diccionarios
        result = dict(result_vector_similarity)
        for w in result_degree_centrality:
            if w in result:
                result[w] += result_degree_centrality[w]
            else:
                result[w] = result_degree_centrality[w]

        # ordenar
        result = dict(sorted(result.items(), key=lambda item: item[1], reverse=True))
        return result
