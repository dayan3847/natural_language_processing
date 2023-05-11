import re
import nltk

nltk.download('punkt') # Descargar el tokenizador

text = "%18``no he podido entrar al TEAM a partir de la plataforma de la UADY, aparezco solo como invitado``"

# trim
text = text.strip()
print(text)

#de