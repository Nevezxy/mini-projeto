import time

from indice_invertido import construir_indice, buscar


# FUNCAO DE BUSCA POR VARREDURA COMPLETA

def busca_varredura(texto, palavra):
    # lista para guardar as linhas onde a palavra foi encontrada
    resultado = []

    # separa o texto em varias linhas
    linhas = texto.split("\n")
    numero = 1

    # sinais que serão retirados durante a busca
    pontuacoes = ".,!?;:()[]{}\"'-"

    # percorre todas as linhas do texto
    for linha in linhas:

        # substitui os sinais de pontuação por espaços
        for sinal in pontuacoes:
            linha = linha.replace(sinal, " ")

        # transforma as palavras em minusculas e separa elas
        palavras = linha.lower().split()

        # verifica se a palavra pesquisada aparece na linha
        if palavra.lower() in palavras:
            # adiciona o numero da linha ao resultado
            resultado.append(numero)

        # passa para a proxima linha
        numero = numero + 1

    return resultado


# TEXTO UTILIZADO NO EXPERIMENTO

texto_base = """Python e dados
Dados e algoritmos
Python e algoritmos
Programação em Python
"""

# repete o texto 2000 vezes para realizar os testes
texto = texto_base * 2000


# PALAVRAS UTILIZADAS NAS CONSULTAS

# palavras escolhidas para testar diferentes tipos de pesquisa
palavras = ["python", "dados", "algoritmos", "programação", "java"]


# MEDINDO A CONSTRUCAO DO INDICE

# registra o horario antes de criar o indice
inicio = time.perf_counter()

indice = construir_indice(texto)

# registra o horario depois da criacaoo
fim = time.perf_counter()

# calcula o tempo gasto em milissegundos
tempo_construcao = (fim - inicio) * 1000


# MEDINDO 1000 BUSCAS POR VARREDURA

# começa a contagem do tempo das buscas
inicio = time.perf_counter()

# realiza 1000 consultas utilizando a varredura completa
for numero in range(1000):
    # escolhe uma palavra da lista para realizar a pesquisa
    palavra = palavras[numero % len(palavras)]
    busca_varredura(texto, palavra)

# finaliza a contagem do tempo
fim = time.perf_counter()

# calcula o tempo total das consultas
tempo_varredura = (fim - inicio) * 1000


# MEDINDO 1000 BUSCAS COM INDICE

# comeca a contagem do tempo das buscas pelo indice
inicio = time.perf_counter()

# realiza 1000 consultas utilizando o indice invertido
for numero in range(1000):
    # escolhe uma palavra da lista para realizar a pesquisa
    palavra = palavras[numero % len(palavras)]
    buscar(indice, palavra)

# finaliza a contagem do tempo
fim = time.perf_counter()

# calcula o tempo total das consultas
tempo_indice = (fim - inicio) * 1000

print("\n===== RESULTADOS =====")

print("Construcao do indice:", round(tempo_construcao, 3), "ms")

print("1000 buscas por varredura:", round(tempo_varredura, 3), "ms")

print("1000 buscas com indice:", round(tempo_indice, 3), "ms")