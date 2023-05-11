import networkx as nx
from typing import List

from src.graphs.GraphReducer import GraphReducer
from src.graphs.Precision import Precision


class PrecisionPagerank(Precision):

    def estimate_input(self, t: str, subset: List[str]) -> dict:
        graph = self.data_set.import_graphs()[t]
        sub_graph = GraphReducer.reduce_graph(graph, subset)
        if len(sub_graph.nodes()) == 0:
            return {}
        try:
            result = nx.pagerank(
                sub_graph,
                # alpha=0.85,
                # personalization=None,
                # max_iter=100,
                # tol=1e-06,
                # nstart=None,
                # weight='weight',
                # dangling=None
            )
        except:
            result = {}

        for w in subset:
            if w in result:
                result.pop(w)
        result = dict(sorted(result.items(), key=lambda item: item[1], reverse=True))
        return result
