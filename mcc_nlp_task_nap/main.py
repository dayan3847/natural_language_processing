from src.graphs.PrecisionSubgraphCentrality import PrecisionSubgraphCentrality
from src.graphs.PrecisionVectorSimilarity import PrecisionVectorSimilarity
from src.graphs.PrecisionVectorSimilarityAndBetweennessCentrality import \
    PrecisionVectorSimilarityAndBetweennessCentrality
from src.graphs.PrecisionVectorSimilarityAndDegreeCentrality import PrecisionVectorSimilarityAndDegreeCentrality
from src.repo import DataSet
from src.graphs.Precision import Precision
from src.graphs.PrecisionBetweennessCentrality import PrecisionBetweennessCentrality
from src.graphs.PrecisionCommunicabilityBetweennessCentrality import PrecisionCommunicabilityBetweennessCentrality
from src.graphs.PrecisionClosenessCentrality import PrecisionClosenessCentrality
from src.graphs.PrecisionEigenvectorCentrality import PrecisionEigenvectorCentrality
from src.graphs.PrecisionCurrentFlowClosenessCentrality import PrecisionCurrentFlowClosenessCentrality
from src.graphs.PrecisionDegreeCentrality import PrecisionDegreeCentrality
from src.graphs.PrecisionPagerank import PrecisionPagerank

if __name__ == '__main__':
    data_set = DataSet.get_instance()
    the_graphs = data_set.import_graphs()
    the_emb = data_set.import_emb()
    the_definitions = data_set.import_definitions()

    # # Betweenness Centrality
    # precision: Precision = PrecisionBetweennessCentrality()
    # # Communicability Betweenness Centrality
    # precision: Precision = PrecisionCommunicabilityBetweennessCentrality()
    # # Closeness Centrality
    # precision: Precision = PrecisionClosenessCentrality()
    # # Eigenvector Centrality
    # precision: Precision = PrecisionEigenvectorCentrality()
    # # Current Flow Closeness Centrality
    # precision: Precision = PrecisionCurrentFlowClosenessCentrality()
    # # Degree Centrality
    # precision: Precision = PrecisionDegreeCentrality()
    # # Pagerank
    # precision: Precision = PrecisionPagerank()
    # Subgraph Centrality
    precision: Precision = PrecisionSubgraphCentrality()
    # # Vector Similarity
    # precision: Precision = PrecisionVectorSimilarity()
    # # Vector Similarity and Degree Centrality
    # precision: Precision = PrecisionVectorSimilarityAndDegreeCentrality()
    # # Vector Similarity and Betweenness Centrality
    # precision: Precision = PrecisionVectorSimilarityAndBetweennessCentrality()

    results = precision.calculate_precisions(the_definitions)
    print(results)
