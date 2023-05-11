from textblob import TextBlob

# Texto de ejemplo
texto = "Juan"

# Procesar el texto con TextBlob
blob = TextBlob(texto)

# Extraer todas las frases nominales (noun phrases) del texto
frases_nominales = blob.noun_phrases

# Iterar sobre las frases nominales y buscar nombres de personas
for frase in frases_nominales:
    palabras = frase.split()
    if len(palabras) > 1 and palabras[0].istitle() and palabras[-1].istitle():
        print(frase)
