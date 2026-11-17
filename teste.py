from indice_invertido import construir_indice

texto = """Python,dados!algoritmos.
Dados e Python.
Programação,programacao

Python Python"""

indice = construir_indice(texto)

for palavra in indice:
    print(palavra, ":", indice[palavra])