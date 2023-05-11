import networkx as nx
from typing import List

from src.graphs.GraphReducer import GraphReducer
from src.graphs.Precision import Precision


class PrecisionClosenessCentrality(Precision):

    def estimate_input(self, t: str, subset: List[str]) -> dict:
        graph = self.data_set.import_graphs()[t]
        sub_graph = GraphReducer.reduce_graph(graph, subset)
        result = nx.closeness_centrality(sub_graph, wf_improved=True, distance="weight")
        for w in subset:
            if w in result:
                result.pop(w)
        result = dict(sorted(result.items(), key=lambda item: item[1], reverse=True))
        return result
