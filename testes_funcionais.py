from indice_invertido import construir_indice, buscar, buscar_e, buscar_ou


# TESTE 1 - CONSTRUCAO DO INDICE

texto = """Python e dados
Dados e algoritmos
Python e algoritmos"""

indice = construir_indice(texto)

# verifica se as palavras foram armazenadas nas linhas corretas
assert indice["python"] == {1, 3}
assert indice["dados"] == {1, 2}
assert indice["algoritmos"] == {2, 3}

print("Teste 1 passou!")


# TESTE 2 - BUSCA SIMPLES

# verifica se a busca encontra as palavras corretamente
assert buscar(indice, "python") == [1, 3]
assert buscar(indice, "java") == []
assert buscar(indice, "PYTHON") == [1, 3]

print("Teste 2 passou!")


# TESTE 3 - BUSCA E

# verifica se apenas as linhas com todas as palavras são retornadas
assert buscar_e(indice, ["python", "dados"]) == [1]
assert buscar_e(indice, ["python", "algoritmos"]) == [3]
assert buscar_e(indice, ["python", "java"]) == []

print("Teste 3 passou!")


# TESTE 4 - BUSCA OU

# verifica se são encontradas as linhas que possuem pelo menos uma palavra
assert buscar_ou(indice, ["python", "dados"]) == [1, 2, 3]
assert buscar_ou(indice, ["python", "java"]) == [1, 3]
assert buscar_ou(indice, ["java", "javascript"]) == []

print("Teste 4 passou!")


# TESTE 5 - TEXTO VAZIO

# verifica se o indice fica vazio quando não existe nenhum texto
indice_vazio = construir_indice("")

assert indice_vazio == {}

print("Teste 5 passou!")


# TESTE 6 - PALAVRAS REPETIDAS

# verifica se palavras repetidas não geram linhas duplicadas
indice_repetido = construir_indice("Python Python python")

assert indice_repetido["python"] == {1}

print("Teste 6 passou!")


# TESTE 7 - LINHAS VAZIAS

# verifica se as linhas vazias continuam sendo contadas
indice_linhas = construir_indice("Python\n\nDados")

assert indice_linhas["python"] == {1}
assert indice_linhas["dados"] == {3}

print("Teste 7 passou!")


# TESTE 8 - PONTUACAO

# verifica se os sinais de pontuação não atrapalham a busca
indice_pontuacao = construir_indice("Python,dados!algoritmos.")

assert indice_pontuacao["python"] == {1}
assert indice_pontuacao["dados"] == {1}
assert indice_pontuacao["algoritmos"] == {1}

print("Teste 8 passou!")


# TESTE 9 - PALAVRAS COM ACENTOS

# verifica se palavras com e sem acento são armazenadas separadamente
indice_acentos = construir_indice("programação programacao")

assert indice_acentos["programação"] == {1}
assert indice_acentos["programacao"] == {1}

print("Teste 9 passou!")


# TESTE 10 - CONSULTAS COM TRES PALAVRAS

# cria um texto para testar buscas com varias palavras ao mesmo tempo
indice_tres = construir_indice(
    "python dados algoritmos\n"
    "python dados\n"
    "algoritmos"
)

# verifica se a busca E encontra somente a linha que possui todas as palavras
assert buscar_e(indice_tres, ["python", "dados", "algoritmos"]) == [1]

# verifica se a busca OU encontra todas as linhas que possuem alguma das palavras
assert buscar_ou(indice_tres, ["python", "dados", "algoritmos"]) == [1, 2, 3]

print("Teste 10 passou!")


print("\nTodos os testes funcionais passaram!")