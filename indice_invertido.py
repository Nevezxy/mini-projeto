def construir_indice(texto):
    # dicionario vazio para armazenar as palavras
    indice = {}

    # separa o texto em varias linhas
    linhas = texto.split("\n")
    numero = 1

    # sinais de pontuação que serão removidos do texto
    pontuacoes = ".,!?;:()[]{}\"'-"

    # percorre cada linha do texto
    for linha in linhas:

        # substitui os sinais de pontuação por espaços
        for sinal in pontuacoes:
            linha = linha.replace(sinal, " ")

        # transforma todas as letras em minusculas e separa as palavras
        palavras = linha.lower().split()

        # percorre as palavras encontradas na linha
        for palavra in palavras:
            # mostra o numero da linha e a palavra encontrada
            print(numero, palavra)

        # aumenta o contador para a proxima linha
        numero = numero + 1

    return indice