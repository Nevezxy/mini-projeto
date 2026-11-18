# Mini-projeto: Índice invertido para busca textual

Projeto desenvolvido para a disciplina de Estruturas de Dados do IFAL.

## Objetivo

Construir um mecanismo simples de busca textual usando um dicionário como tabela hash e conjuntos para guardar os números das linhas em que cada palavra aparece. O projeto também compara a busca com índice invertido e a busca por varredura completa.

## Arquivos do projeto

- `indice_invertido.py`: construção do índice e funções de busca simples, E e OU.
- `main.py`: menu para realizar consultas.
- `testes_funcionais.py`: testes automatizados.
- `experimentos1.py`: primeira comparação de desempenho com 1.000 consultas.
- `experimantos2.py`: segunda comparação com 1, 10, 100 e 1.000 consultas. O nome está mantido igual ao arquivo atualmente publicado no repositório.
- `teste.py`: exemplos simples utilizados durante o desenvolvimento.
- `RELATORIO.md`: resultados, análises e respostas às seis questões.
- `DIARIO_IA.md`: registro resumido do uso de inteligência artificial.

## Requisitos

- Python 3.10 ou superior.
- Não é necessário instalar pacotes externos.

## Como executar

Abra o terminal na pasta do projeto.

### Menu de consultas

```bash
python main.py
```

### Testes funcionais

```bash
python testes_funcionais.py
```

### Experimentos

```bash
python experimentos1.py
python experimantos2.py
```

Os tempos variam conforme o computador. Para o relatório definitivo, utilize os resultados medidos no computador em que os experimentos foram executados.

## Como funciona

A função `construir_indice(texto)` separa o texto em linhas, começa a numeração em 1, transforma as palavras em letras minúsculas e retira sinais de pontuação. Cada palavra é uma chave do dicionário e seu valor é um conjunto (`set`) com os números das linhas em que aparece.

- `buscar(indice, palavra)`: linhas em que aparece uma palavra.
- `buscar_e(indice, palavras)`: linhas que contêm todas as palavras.
- `buscar_ou(indice, palavras)`: linhas que contêm pelo menos uma das palavras.

As funções de busca retornam listas ordenadas e não recebem dados pelo teclado nem imprimem resultados.
