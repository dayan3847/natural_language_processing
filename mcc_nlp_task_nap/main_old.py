from typing import List

from gensim.models import KeyedVectors

from src.graphs.GraphAlgorithms import GraphAlgorithms
from src.graphs.GraphReducer import GraphReducer
from src.graphs.Precision import Precision
from src.graphs.PrecisionCommunicabilityBetweennessCentrality import PrecisionCommunicabilityBetweennessCentrality
from src.graphs.PrecisionBetweennessCentrality import PrecisionBetweennessCentrality
from src.model.Definition import Definition
from src.repo import DataSet
from src.tools.Tools import Tools


def build_definitions_graph(graphs, definitions: List[Definition]):
    total: int = 0
    p = {
        'frequency': [0, 0, 0],
        'time': [0, 0, 0],
        'association': [0, 0, 0],
        'communicability': [0, 0, 0],
        'degree': [0, 0, 0],
    }
    for definition in definitions:
        print('\033[32m' + f'Input: {definition.word_input}' + '\033[0m')
        for word_output in definition.word_outputs:
            print('\033[33m' + f'Output: {word_output}' + '\033[0m')
            # Frequency
            # btc = GraphAlgorithms.bt_centrality(graphs['frequency'], word_output)
            # btc = GraphAlgorithms.closeness_centrality(graphs['frequency'], word_output)
            btc = GraphAlgorithms.eigenvector_centrality(graphs['frequency'], word_output)
            # btc = GraphAlgorithms.current_flow_closeness_centrality(graphs['frequency'], word_output)
            # btc = GraphAlgorithms.pagerank(graphs['frequency'], word_output)
            p['frequency'][0] += Tools.precision(definition.word_input, btc, 1)
            p['frequency'][1] += Tools.precision(definition.word_input, btc, 3)
            p['frequency'][2] += Tools.precision(definition.word_input, btc, 5)
            print('\033[35m' + str(btc) + '\033[0m')
            # Time
            # btc = GraphAlgorithms.bt_centrality(graphs['time'], word_output)
            # btc = GraphAlgorithms.closeness_centrality(graphs['time'], word_output)
            btc = GraphAlgorithms.eigenvector_centrality(graphs['time'], word_output)
            # btc = GraphAlgorithms.current_flow_closeness_centrality(graphs['time'], word_output)
            # btc = GraphAlgorithms.pagerank(graphs['time'], word_output)
            p['time'][0] += Tools.precision(definition.word_input, btc, 1)
            p['time'][1] += Tools.precision(definition.word_input, btc, 3)
            p['time'][2] += Tools.precision(definition.word_input, btc, 5)
            print('\033[35m' + str(btc) + '\033[0m')
            # Association
            # btc = GraphAlgorithms.bt_centrality(graphs['association'], word_output)
            # btc = GraphAlgorithms.closeness_centrality(graphs['association'], word_output)
            btc = GraphAlgorithms.eigenvector_centrality(graphs['association'], word_output)
            # btc = GraphAlgorithms.current_flow_closeness_centrality(graphs['association'], word_output)
            # btc = GraphAlgorithms.pagerank(graphs['association'], word_output)
            p['association'][0] += Tools.precision(definition.word_input, btc, 1)
            p['association'][1] += Tools.precision(definition.word_input, btc, 3)
            p['association'][2] += Tools.precision(definition.word_input, btc, 5)
            print('\033[35m' + str(btc) + '\033[0m')
            # # Communicability
            # btc = GraphAlgorithms.com_bt_centrality(graphs['frequency'], word_output)
            # p['communicability'][0] += Tools.precision(definition.word_input, btc, 1)
            # p['communicability'][1] += Tools.precision(definition.word_input, btc, 3)
            # p['communicability'][2] += Tools.precision(definition.word_input, btc, 5)
            # print('\033[35m' + str(btc) + '\033[0m')
            # # Degree
            # btc = GraphAlgorithms.degree_centrality(graphs['frequency'], word_output)
            # p['degree'][0] += Tools.precision(definition.word_input, btc, 1)
            # p['degree'][1] += Tools.precision(definition.word_input, btc, 3)
            # p['degree'][2] += Tools.precision(definition.word_input, btc, 5)
            # print('\033[35m' + str(btc) + '\033[0m')
            total += 1
    for k in p.keys():
        for i in range(3):
            p[k][i] /= total
    print(p)


def build_definitions_graph2(definitions: List[Definition], emb_dic):
    total: int = 0
    p = {
        'frequency': [0, 0, 0],
        'time': [0, 0, 0],
        'association': [0, 0, 0],
    }
    for definition in definitions:
        print('\033[32m' + f'Input: {definition.word_input}' + '\033[0m')
        for word_output in definition.word_outputs:
            # frequency
            print('\033[33m' + f'Output: {word_output}' + '\033[0m')
            sum_frequency = Tools.suma_palablas(word_output, emb_dic['frequency'])
            btc = emb_dic['frequency'].most_similar([sum_frequency], topn=20)
            btc = Tools.convert_to_dict(btc)
            # eliminar palablas de la definicion
            for w in word_output:
                if w in btc:
                    # del btc[w]
                    btc.pop(w)
            p['frequency'][0] += Tools.precision(definition.word_input, btc, 1)
            p['frequency'][1] += Tools.precision(definition.word_input, btc, 3)
            p['frequency'][2] += Tools.precision(definition.word_input, btc, 5)
            print('\033[35m' + str(btc) + '\033[0m')
            # time
            sum_time = Tools.suma_palablas(word_output, emb_dic['time'])
            btc = emb_dic['time'].most_similar([sum_time], topn=5)
            btc = Tools.convert_to_dict(btc)
            # eliminar palablas de la definicion
            for w in word_output:
                if w in btc:
                    # del btc[w]
                    btc.pop(w)
            p['time'][0] += Tools.precision(definition.word_input, btc, 1)
            p['time'][1] += Tools.precision(definition.word_input, btc, 3)
            p['time'][2] += Tools.precision(definition.word_input, btc, 5)
            print('\033[35m' + str(btc) + '\033[0m')
            # association
            sum_association = Tools.suma_palablas(word_output, emb_dic['association'])
            btc = emb_dic['association'].most_similar([sum_association], topn=5)
            btc = Tools.convert_to_dict(btc)
            # eliminar palablas de la definicion
            for w in word_output:
                if w in btc:
                    # del btc[w]
                    btc.pop(w)
            p['association'][0] += Tools.precision(definition.word_input, btc, 1)
            p['association'][1] += Tools.precision(definition.word_input, btc, 3)
            p['association'][2] += Tools.precision(definition.word_input, btc, 5)
            print('\033[35m' + str(btc) + '\033[0m')
            total += 1
    for k in p.keys():
        for i in range(3):
            p[k][i] /= total
    print(p)


if __name__ == '__main__':
    data_set = DataSet()
    # Import Definitions
    the_definitions = data_set.import_definitions()

    # Import Graphs
    the_graphs = data_set.import_graphs()
    # print('Frequency ' + str(the_graphs['frequency']))
    # print('Time ' + str(the_graphs['time']))
    # print('Association ' + str(the_graphs['association']))
    # Build Graphs
    # build_definitions_graph(the_graphs, the_definitions)
    ### 'frequency': [0.34782608695652173, 0.572463768115942, 0.6594202898550725],

    # communicability old, el que estaba en la tabla
    # 0.2210144928
    # 0.4275362319
    # 0.5217391304
    # communicability nuevo
    # {'Association': {'1': 0.22826086956521738, '3': 0.4311594202898551, '5': 0.5181159420289855}}

    print('Cargar modelos')
    wvF_frequency = KeyedVectors.load_word2vec_format(f'./corpus/emb/frequency.emb', binary=False)
    wvF_time = KeyedVectors.load_word2vec_format(f'./corpus/emb/time.emb', binary=False)
    wvF_association = KeyedVectors.load_word2vec_format(f'./corpus/emb/association.emb', binary=False)

    the_emb = {
        'frequency': wvF_frequency,
        'time': wvF_time,
        'association': wvF_association,
    }
    build_definitions_graph2(the_definitions, the_emb)
