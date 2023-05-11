from typing import List

from src.model.Definition import Definition
from src.repo import DataSet
from src.tools.Tools import Tools


class Precision:
    def __init__(self):
        self.data_set: DataSet = DataSet.get_instance()
        self.verbose = True

    @staticmethod
    def get_types():
        return ['frequency', 'time', 'association']

    @staticmethod
    def get_k_values():
        return [1, 3, 5]

    def calculate_precisions(self, definitions: List[Definition]) -> dict[str, dict[str, float]]:
        types = self.get_types()
        results = {}

        for t in types:
            results[t] = self.calculate_precisions_by_type(definitions, t)

        return results

    def calculate_precisions_by_type(self, definitions: List[Definition], t: str) -> dict[str, float]:
        result: dict[str, float] = {}
        total: int = 0
        ks = self.get_k_values()
        for k in ks:
            result[str(k)] = 0
        for definition in definitions:
            self.print('\033[32m' + f'Input: {definition.word_input}' + '\033[0m')
            for word_output in definition.word_outputs:
                self.print('\033[33m' + f'Output: {word_output}' + '\033[0m')
                dic = self.estimate_input(t, word_output)
                self.print('\033[35m' + str(dic) + '\033[0m')
                for k in ks:
                    result[str(k)] += Tools.precision(definition.word_input, dic, k)
                total += 1
        for k in ks:
            result[str(k)] /= total
        return result

    def estimate_input(self, t: str, subset: List[str]) -> dict:
        pass

    def print(self, text: str):
        if self.verbose:
            print(text)
