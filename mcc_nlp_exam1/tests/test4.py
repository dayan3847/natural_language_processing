import freeling

# Configurar Freeling
freeling.util_init_locale("default")
op = freeling.maco_options("es")
op.set_active_modules(False, True, False, False, False, False, False, False, False, False, False)
tk = freeling.tokenizer("es")
sp = freeling.splitter("es")
sid = sp.open_session()
mf = freeling.maco(op)
mf.set_active_options(False, True, True, True, True, True, False, True, True, True, True, True)
tg = freeling.hmm_tagger("es")
sen = freeling.senses("es")
parser = freeling.chart_parser("es")
dep = freeling.dep_txala("es")
ner = freeling.ner("es")

# Texto de ejemplo
texto = "Juan Pérez es un famoso escritor español."

# Procesar el texto con Freeling
l = tk.tokenize(texto)
ls = sp.split(sid, l)
ls = mf.analyze(ls)
ls = tg.analyze(ls)
ls = sen.analyze(ls)
ls = parser.analyze(ls)
ls = dep.analyze(ls)
ls = ner.analyze(ls)

# Iterar sobre las entidades nombradas en el documento
for s in ls:
    for w in s:
        # Si la palabra es una entidad nombrada y es una persona, imprimir su forma canónica
        if w.get_tag().startswith("NP") and ner.get_name_entity_label(w) == "PERSON":
            print(w.get_form())
