import time

from indice_invertido import construir_indice, buscar


# BUSCA POR VARREDURA COMPLETA

def busca_varredura(texto, palavra):
    resultado = []

    linhas = texto.split("\n")
    numero = 1

    pontuacoes = ".,!?;:()[]{}\"'-"

    for linha in linhas:
        for sinal in pontuacoes:
            linha = linha.replace(sinal, " ")

        palavras = linha.lower().split()

        if palavra.lower() in palavras:
            resultado.append(numero)

        numero = numero + 1

    return resultado


# TEXTO DO EXPERIMENTO

texto_base = """Python e dados
Dados e algoritmos
Python e algoritmos
Programação em Python
"""

texto = texto_base * 2000


# PALAVRAS UTILIZADAS NAS PESQUISAS

palavras = [
    "python",
    "dados",
    "algoritmos",
    "programação",
    "java"
]

quantidades = [1, 10, 100, 1000]


# REALIZANDO OS EXPERIMENTOS

print("===== EXPERIMENTO 2 =====")

for quantidade in quantidades:

    tempos_varredura = []
    tempos_indice = []

    # REPETINDO CADA MEDICAO 3 VEZES

    for repeticao in range(3):

        # MEDINDO A VARREDURA COMPLETA

        inicio = time.perf_counter()

        for numero in range(quantidade):
            palavra = palavras[numero % len(palavras)]
            busca_varredura(texto, palavra)

        fim = time.perf_counter()

        tempo = (fim - inicio) * 1000
        tempos_varredura.append(tempo)


        # MEDINDO A CONSTRUCAO E AS BUSCAS

        inicio = time.perf_counter()

        indice = construir_indice(texto)

        for numero in range(quantidade):
            palavra = palavras[numero % len(palavras)]
            buscar(indice, palavra)

        fim = time.perf_counter()

        tempo = (fim - inicio) * 1000
        tempos_indice.append(tempo)


    # CALCULANDO AS MEDIANAS

    tempos_varredura.sort()
    tempos_indice.sort()

    mediana_varredura = tempos_varredura[1]
    mediana_indice = tempos_indice[1]


    # MOSTRANDO OS RESULTADOS

    print("\nQuantidade de consultas:", quantidade)

    print("Varredura:",
          round(mediana_varredura, 3), "ms")

    print("Construcao + indice:",
          round(mediana_indice, 3), "ms")