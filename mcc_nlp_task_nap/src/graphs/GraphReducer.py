from networkx import Graph


class GraphReducer:

    @staticmethod
    def reduce_graph(graph: Graph, subset: list) -> Graph:
        return GraphReducer.reduce_graph_1(graph, subset)
        # return GraphReducer.reduce_graph_2(graph, subset)

    # no tiene en cuenta conexiones entre nodos vecinos
    @staticmethod
    def reduce_graph_1(graph: Graph, subset: list) -> Graph:
        sub_graph = Graph()
        for node in subset:
            if node not in graph.nodes():
                continue
            for neighbor in graph.neighbors(node):
                weight = graph[node][neighbor]['weight']
                sub_graph.add_edge(node, neighbor, weight=weight)
        return sub_graph

    @staticmethod
    def reduce_graph_2(grafo_original, subconjunto):
        nuevos_nodos = []
        nuevos_nodos.extend(subconjunto)
        for nodo in subconjunto:
            if nodo not in grafo_original.nodes():
                continue
            vecinos = grafo_original[nodo]
            for vecino in vecinos:
                nuevos_nodos.append(vecino)
        grafo_reducido = grafo_original.subgraph(nuevos_nodos)
        # grafica(grafo_reducido)
        return grafo_reducido
