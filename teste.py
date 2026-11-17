from indice_invertido import construir_indice, buscar

texto = """Python e dados
Dados e algoritmos
Python e algoritmos"""

indice = construir_indice(texto)

print(buscar(indice, "python"))
print(buscar(indice, "dados"))
print(buscar(indice, "java"))
print(buscar(indice, "PYTHON"))