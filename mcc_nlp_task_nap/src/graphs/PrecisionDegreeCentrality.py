import networkx as nx
from typing import List

from src.graphs.GraphReducer import GraphReducer
from src.graphs.Precision import Precision


class PrecisionDegreeCentrality(Precision):

    @staticmethod
    def get_types():
        return ['frequency']

    def estimate_input(self, t: str, subset: List[str]) -> dict:
        graph = self.data_set.import_graphs()[t]
        sub_graph = GraphReducer.reduce_graph(graph, subset)
        if len(sub_graph.nodes()) == 0:
            return {}
        try:
            result = nx.degree_centrality(sub_graph)
        except:
            result = {}

        for w in subset:
            if w in result:
                result.pop(w)
        result = dict(sorted(result.items(), key=lambda item: item[1], reverse=True))
        return result
