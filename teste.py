from indice_invertido import *

texto = """Python e dados
Dados e algoritmos
Python e algoritmos
Python dados algoritmos"""

indice = construir_indice(texto)

print(buscar_ou(indice, ["python", "dados"]))
print(buscar_ou(indice, ["dados", "algoritmos"]))
print(buscar_ou(indice, ["python", "java"]))
print(buscar_ou(indice, ["java", "c++"]))
print(buscar_ou(indice, ["python", "dados", "algoritmos"]))