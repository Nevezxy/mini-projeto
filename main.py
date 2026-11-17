from indice_invertido import construir_indice, buscar, buscar_e, buscar_ou

texto = """Python é uma linguagem de programação.
Estruturas de dados são importantes.
Python utiliza estruturas de dados.
Algoritmos utilizam dados.
Programação em Python é interessante."""

indice = construir_indice(texto)

while True:
    print("\n===== BUSCA TEXTUAL =====")
    print("1 - Busca simples")
    print("2 - Busca E")
    print("3 - Busca OU")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        print("Programa encerrado.")
        break

    # realiza uma busca por apenas uma palavra
    elif opcao == "1":
        palavra = input("Digite uma palavra: ")
        resultado = buscar(indice, palavra)

        # mostra as linhas onde a palavra foi encontrada
        print("Linhas encontradas:", resultado)

    # realiza a busca E, procurando palavras que aparecem juntas
    elif opcao == "2":
        entrada = input("Digite as palavras separadas por espaço: ")
        palavras = entrada.split()

        # verifica se foram digitadas pelo menos duas palavras
        if len(palavras) < 2:
            print("Digite pelo menos duas palavras.")
        else:
            resultado = buscar_e(indice, palavras)

            # mostra as linhas que possuem todas as palavras
            print("Linhas encontradas:", resultado)

    # realiza a busca OU, procurando linhas que tenham alguma das palavras
    elif opcao == "3":
        entrada = input("Digite as palavras separadas por espaço: ")
        palavras = entrada.split()

        # verifica se foram digitadas pelo menos duas palavras
        if len(palavras) < 2:
            print("Digite pelo menos duas palavras.")
        else:
            resultado = buscar_ou(indice, palavras)

            # mostra as linhas que possuem pelo menos uma das palavras
            print("Linhas encontradas:", resultado)

    else:
        print("Opção inválida.")