import os
import nltk
import xlrd

from typing import List
from gensim.models import KeyedVectors
from networkx import Graph

from src.model.Definition import Definition


class DataSet:

    def __init__(self, corpus_path: str = './corpus'):
        self.graphs: dict[str, Graph] = {}
        self.definitions: List[Definition] = []
        self.emb: dict[str, KeyedVectors] = {}

        self.path_file_nap: str = f'{corpus_path}/nap/NAP.xls'
        self.path_folder_definitions: str = f'{corpus_path}/freeling_definitions/'
        self.path_folder_emb: str = f'{corpus_path}/emb/'

        self.ignore_words: List[str] = ['--PALABRAS--', '', '=', '*']

        self.types: List[str] = ['frequency', 'time', 'association']

    def import_graphs(self) -> dict[str, Graph]:
        if 0 < len(self.graphs):
            return self.graphs
        for t in self.types:
            self.graphs[t] = Graph()

        workbook = xlrd.open_workbook(self.path_file_nap)
        sheet = workbook.sheet_by_index(0)
        count_rows = sheet.nrows
        word_input: str = ''
        for row in range(count_rows):
            cell = sheet.cell(row, 0)
            cell_value: str = str(cell.value).strip()
            cell_value_lem: str = str(sheet.cell(row, 4).value)
            if '======' == cell_value:
                word_input = ''
                continue
            elif cell_value in self.ignore_words:
                continue
            elif '' == word_input:
                word_input = cell_value_lem
            else:
                # frequency
                frequency: float = float(sheet.cell(row, 1).value)
                frequency_weight: float = 1 / frequency
                self.graphs['frequency'].add_edge(word_input, cell_value_lem, weight=frequency_weight)
                # time
                time: float = float(sheet.cell(row, 2).value)
                self.graphs['time'].add_edge(word_input, cell_value_lem, weight=time)
                # association
                association: float = float(sheet.cell(row, 3).value)
                association_weight: float = 100 - association
                self.graphs['association'].add_edge(word_input, cell_value_lem, weight=association_weight)
        return self.graphs

    @staticmethod
    def clean_lematize(sentence: str):
        sentence = sentence.strip()
        result: str = ''
        stopwords = nltk.corpus.stopwords.words('spanish')
        words = sentence.split()
        for word in words:
            if word in stopwords:
                continue
            # doc = nlp(word)
            # result += doc[0].lemma_+ " "
            result += word + ' '
        return result

    def import_definitions(self) -> List[Definition]:
        if len(self.definitions) > 0:
            return self.definitions
        directory: str = self.path_folder_definitions
        self.definitions: List[Definition] = []
        for file_name in os.listdir(directory):
            if not file_name.endswith('.txt'):
                continue

            file_data = open(directory + file_name, encoding="utf8")
            lines = file_data.readlines()
            definition = Definition()
            definition.word_input = str(lines[0]).lower().strip()
            for line in lines[1:]:
                line = line.strip()
                if '' == line:
                    continue
                line = self.clean_lematize(line)
                definition.word_outputs.append(line.split())
            self.definitions.append(definition)

        return self.definitions

    def import_emb(self) -> dict[str, KeyedVectors]:
        if 0 == len(self.emb):
            for t in self.types:
                self.emb[t] = KeyedVectors.load_word2vec_format(f'{self.path_folder_emb}/{t}.emb', binary=False)
        return self.emb

    __instance: 'DataSet' = None

    @staticmethod
    def get_instance(corpus_path: str = './corpus') -> 'DataSet':
        if DataSet.__instance is None:
            DataSet.__instance = DataSet(corpus_path)
        return DataSet.__instance
