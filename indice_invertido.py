def construir_indice(texto):
    # dicionario vazio para guardar as palavras e suas linhas
    indice = {}

    # separa o texto em varias linhas
    linhas = texto.split("\n")
    numero = 1

    # sinais de pontuação que serão substituidos por espaços
    pontuacoes = ".,!?;:()[]{}\"'-"

    # percorre todas as linhas do texto
    for linha in linhas:

        # remove os sinais de pontuação da linha
        for sinal in pontuacoes:
            linha = linha.replace(sinal, " ")

        # deixa todas as palavras em minusculo e separa elas
        palavras = linha.lower().split()

        # percorre cada palavra encontrada
        for palavra in palavras:

            # verifica se a palavra ainda não está no dicionario
            if palavra not in indice:
                # cria um conjunto vazio para guardar os numeros das linhas
                indice[palavra] = set()

            # adiciona o numero da linha onde a palavra foi encontrada
            indice[palavra].add(numero)

        # passa para a proxima linha
        numero = numero + 1

    # retorna o indice completo
    return indice

def buscar(indice, palavra):
    # transforma a palavra em minuscula para facilitar a busca
    palavra = palavra.lower()

    # verifica se a palavra existe no indice
    if palavra in indice:
        # pega os numeros das linhas onde a palavra aparece
        linhas = indice[palavra]

        # organiza os numeros das linhas em ordem crescente
        return sorted(linhas)
    else:
        # retorna uma lista vazia caso a palavra não seja encontrada
        return []
    
def buscar_e(indice, palavras):
    # verifica se a lista de palavras esta vazia
    if len(palavras) == 0:
        return []

    # pega as linhas onde aparece a primeira palavra
    resultado = set(buscar(indice, palavras[0]))

    # percorre todas as palavras recebidas na busca
    for palavra in palavras:
        # pega as linhas onde a palavra aparece
        linhas = set(buscar(indice, palavra))

        # mantem apenas as linhas que possuem todas as palavras
        resultado = resultado & linhas

    return sorted(resultado)

def buscar_ou(indice, palavras):
    # cria um conjunto vazio para guardar as linhas encontradas
    resultado = set()

    # percorre todas as palavras recebidas na busca
    for palavra in palavras:
        # pega as linhas onde a palavra aparece
        linhas = set(buscar(indice, palavra))

        # junta as linhas encontradas sem repetir numeros
        resultado = resultado | linhas

    return sorted(resultado)