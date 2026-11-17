def construir_indice(texto):
    # dicionario vazio onde as palavras serão armazenadas
    indice = {}

    # separa o texto em varias linhas
    linhas = texto.split("\n")
    numero = 1

    # percorre todas as linhas do texto
    for linha in linhas:
        # mostra o numero e o conteudo de cada linha
        print(numero, linha)

        # passa para o numero da proxima linha
        numero = numero + 1

    # retorna o indice criado
    return indice