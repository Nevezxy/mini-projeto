from indice_invertido import *

texto = """Python e dados
Dados e algoritmos
Python e algoritmos
Python dados algoritmos"""

indice = construir_indice(texto)

print(buscar_e(indice, ["python", "dados"]))
print(buscar_e(indice, ["dados", "algoritmos"]))
print(buscar_e(indice, ["python", "java"]))
print(buscar_e(indice, ["python", "dados", "algoritmos"]))