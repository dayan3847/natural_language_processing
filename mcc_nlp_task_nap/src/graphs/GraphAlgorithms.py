import networkx as nx
from typing import List

from src.graphs.GraphReducer import GraphReducer


class GraphAlgorithms:

    @staticmethod
    def bt_centrality(graph: nx.Graph, subset: List[str]) -> dict:
        sub_graph = GraphReducer.reduce_graph(graph, subset)
        result = nx.betweenness_centrality(sub_graph, normalized=True, weight="weight")
        for w in subset:
            if w in result:
                result.pop(w)
        result = dict(sorted(result.items(), key=lambda item: item[1], reverse=True))
        return result

    @staticmethod
    def com_bt_centrality(graph: nx.Graph, subset: List[str]) -> dict:
        sub_graph = GraphReducer.reduce_graph(graph, subset)
        result = nx.communicability_betweenness_centrality(sub_graph)
        for w in subset:
            if w in result:
                result.pop(w)
        result = dict(sorted(result.items(), key=lambda item: item[1], reverse=True))
        return result

    @staticmethod
    def closeness_centrality(graph: nx.Graph, subset: List[str]) -> dict:
        sub_graph = GraphReducer.reduce_graph(graph, subset)
        result = nx.closeness_centrality(sub_graph, wf_improved=True, distance="weight")
        for w in subset:
            if w in result:
                result.pop(w)
        result = dict(sorted(result.items(), key=lambda item: item[1], reverse=True))
        return result

    @staticmethod
    def eigenvector_centrality(graph: nx.Graph, subset: List[str]) -> dict:
        sub_graph = GraphReducer.reduce_graph(graph, subset)
        if len(sub_graph.nodes()) == 0:
            return {}

        result = nx.eigenvector_centrality(sub_graph, max_iter=10000, weight="weight")
        for w in subset:
            if w in result:
                result.pop(w)
        result = dict(sorted(result.items(), key=lambda item: item[1], reverse=True))
        return result

    @staticmethod
    def current_flow_closeness_centrality(graph: nx.Graph, subset: List[str]) -> dict:
        sub_graph = GraphReducer.reduce_graph(graph, subset)
        if len(sub_graph.nodes()) == 0:
            return {}
        try:
            result = nx.current_flow_closeness_centrality(sub_graph, weight="weight")
        except:
            result = {}

        for w in subset:
            if w in result:
                result.pop(w)
        result = dict(sorted(result.items(), key=lambda item: item[1], reverse=True))
        return result

    @staticmethod
    def degree_centrality(graph: nx.Graph, subset: List[str]) -> dict:
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

    @staticmethod
    def pagerank(graph: nx.Graph, subset: List[str]) -> dict:
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
