from typing import List

import nltk
from pandas import DataFrame
import pandas as pd
import spacy
import re
import openpyxl


# ! python -m spacy download es_core_news_sm

class Exam1:
    def __init__(self):
        self.corpus: List[str] = []
        self.original_corpus: List[str] = []
        self.__names: List = []
        self.nlp = spacy.load("es_core_news_sm")

        self.corpus_no_names = []

    def import_corpus(self, file: str = 'corpus_primer_parcial.xlsx'):
        df: DataFrame = pd.read_excel(file)
        self.corpus = df.iloc[:, 0].tolist()
        # self.corpus = [self.corpus[0]]
        self.original_corpus = self.corpus.copy()

        # import corpus_no_names.txt
        with open('corpus_no_names.txt', 'r') as f:
            self.corpus_no_names = f.read().splitlines()

    def get_colorized_corpus(self) -> List[str]:
        result = []
        for text in self.corpus:
            text = text.replace('$phone$', "\033[1;33;40m$phone$\033[0m")
            text = text.replace('$person$', "\033[1;33;40m$person$\033[0m")
            text = text.replace('$email$', "\033[1;33;40m$email$\033[0m")
            text = text.replace('$username$', "\033[1;33;40m$username$\033[0m")
            text = text.replace('$ip$', "\033[1;33;40m$ip$\033[0m")
            result.append(text)
        return result

    # Exercise 1
    def to_lower(self):
        for i in range(len(self.corpus)):
            self.corpus[i] = self.corpus[i].lower()

    # Exercise 2
    def fix_text(self, text: str) -> str:
        # garantizar espacios en los paréntesis
        text = re.sub(r'(\S)\(', r'\1 (', text)
        text = re.sub(r'\)(\S)', r') \1', text)
        # garantizar espacios en los guiones si es adyacente a una letra
        # text = re.sub(r'-(\w)', r'- \1', text)
        # text = re.sub(r'(\w)-', r'\1 -', text)
        text = re.sub(r'(\S)-', r'\1 -', text)
        text = re.sub(r'-(\S)', r'- \1', text)
        # capitalize the first letter
        text_lines = text.splitlines()
        text = ''
        for line in text_lines:
            if 0 < len(line):
                text += str(line[0].upper() + line[1:]).strip()
            text += ' \n'
        # print()
        # print("\033[1;35;40m Fixed to extract names: \033[0m")
        # print(text)
        # print()
        return text

    def get_names(self) -> List:
        if 0 == len(self.__names):
            for text in self.corpus:
                result = set()
                text = self.fix_text(text)
                doc = self.nlp(text)
                # for line in text_lines:
                for ent in doc.ents:
                    ent_srt = str(ent.text)
                    if 'PER' == ent.label_ and ent_srt.lower() not in self.corpus_no_names:
                        if -1 == ent_srt.find('\n'):
                            result.add(ent.text)
                        else:
                            result = self.re_analyze(ent_srt, result)

                self.__names.append(result)
        return self.__names

    def re_analyze(self, ent_srt, result):
        ent_srt = ent_srt.replace('\n', '. ')
        doc = self.nlp(ent_srt)
        for ent in doc.ents:
            ent_srt = str(ent.text)
            if 'PER' == ent.label_ and ent_srt.lower() not in self.corpus_no_names:
                result.add(ent.text)
        return result

    # Exercise 2
    def replace_names(self):
        names = self.get_names()
        for i in range(len(self.corpus)):
            text = self.corpus[i]
            for name in names[i]:
                text = text.replace(name, '$person$')
            # replace username
            for name in names[i]:
                single_names = name.split()
                if 1 >= len(single_names):
                    continue
                for single_name0 in single_names:
                    for single_name1 in single_names:
                        if single_name0 == single_name1:
                            continue
                        username = f'{single_name0}.{single_name1}'
                        username = username.lower()
                        text = text.replace(username, '$username$')
            # replace single names
            for name in names[i]:
                single_names = name.split()
                if 1 >= len(single_names):
                    continue
                for single_name in single_names:
                    if 4 > len(single_name):
                        continue
                    text = text.replace(single_name, '$person$')
            self.corpus[i] = text

    # Exercise 3
    def remove_garbage(self):
        for i in range(len(self.corpus)):
            text = self.corpus[i]
            text = re.sub(r'(`)\1+', '', text)
            text = re.sub(r'(%\d{2})', '', text)
            self.corpus[i] = text

    # Exercise 4
    def remove_phone_numbers(self):
        for i in range(len(self.corpus)):
            text = self.corpus[i]
            text = re.sub(r'([\(\s])\d{10}([\)\s])', r'\1$phone$\2', text)
            self.corpus[i] = text

    # Exercise 5
    def remove_emails(self):
        for i in range(len(self.corpus)):
            text = self.corpus[i]
            text = re.sub(r'([\w\.-]+@[\w\.-]+)', r'$email$', text)
            self.corpus[i] = text

    # Exercise Additional
    def remove_ip(self):
        for i in range(len(self.corpus)):
            text = self.corpus[i]
            text = re.sub(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", r'$ip$', text)
            self.corpus[i] = text

    def print_corpus_changes(self):
        for i in range(len(self.corpus)):
            print()
            print()
            print()
            print(f'\033[1;32;40m {"-" * 10} Text: {str(i + 1)} {"-" * 10} \033[0m')
            print()
            print("\033[1;35;40m Original: \033[0m")
            print(self.original_corpus[i])
            print()
            print("\033[1;35;40m Final: \033[0m")
            colorized_corpus = self.get_colorized_corpus()
            print(colorized_corpus[i])

    # create a new file with the corpus
    def export_corpus(self, prefix: str = ''):
        for i in range(len(self.corpus)):
            filename = f'./output/text_{i + 1}{prefix}.txt'
            with open(filename, 'w') as f:
                f.write(self.corpus[i])


if __name__ == '__main__':
    exam1 = Exam1()

    print("\033[1;34;40m 0. Importar corpus \033[0m")
    exam1.import_corpus()

    print("\033[1;34;40m 0. Exportar corpus (estado inicial) \033[0m")
    exam1.export_corpus()

    # Exercise 3
    print("\033[1;34;40m 3. Eliminar códigos que sean basura, ejemplo: %18``.\033[0m")
    exam1.remove_garbage()

    # Exercise 4
    print("\033[1;34;40m 4. Eliminar números telefónicos y sustituirlos por #Teléfono.\033[0m")
    exam1.remove_phone_numbers()

    # Exercise 5
    print("\033[1;34;40m 5. Eliminar correos electrónicos y sustituirlos por #Email.\033[0m")
    exam1.remove_emails()

    # Exercise Additional
    print("\033[1;34;40m 6. Eliminar direcciones IP y sustituirlos por #IP.\033[0m")
    exam1.remove_ip()

    # Exercise 2
    print(
        "\033[1;34;40m 2. Quitar los nombres propios que aparezcan y sustituirlos por una etiqueta llamada #Persona. \033[0m")
    exam1.replace_names()

    # Exercise 1
    print("\033[1;34;40m 1. Pasar a minúsculas todo el texto \033[0m")
    exam1.to_lower()

    print("\033[1;34;40m 0. Exportar corpus (estado final) \033[0m")
    # exam1.export_corpus()
    exam1.export_corpus('_final')

    exam1.print_corpus_changes()
