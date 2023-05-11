import nltk
from nltk.corpus import wordnet

# Descargar la lista de palabras de WordNet
nltk.download('wordnet')

# Lista de palabras a verificar
words = ['car', 'love', 'tree', 'run']
# agregar una palabra que no es un sustantivo
words.append('the')

# Verificar si cada palabra es un sustantivo
for word in words:
    synsets = wordnet.synsets(word)
    if synsets:
        for synset in synsets:
            if 'n' in synset.pos():
                print(f"{word} es un sustantivo")
                break
    else:
        print(f"{word} no es un sustantivo")
