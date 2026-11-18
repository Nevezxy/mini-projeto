# Mini-projeto: Índice invertido para busca textual

Projeto desenvolvido para a disciplina de Estruturas de Dados do curso de Bacharelado em Sistemas de Informação do IFAL.

## Objetivo

Construir um mecanismo simples de busca textual usando um dicionário como tabela hash e conjuntos para guardar os números das linhas em que cada palavra aparece. O projeto também compara a busca com índice invertido e a busca por varredura completa.

## Arquivos

- `indice_invertido.py`: construção do índice e funções de busca simples, E e OU.
- `main.py`: menu para realizar consultas em um texto de exemplo.
- `testes_funcionais.py`: testes automatizados das funções principais.
- `experimento1.py`: primeira comparação de desempenho com 1.000 consultas.
- `experimento2.py`: comparação com 1, 10, 100 e 1.000 consultas, usando três medições e mediana.
- `teste.py`: exemplos simples de chamadas das funções durante o desenvolvimento.
- `RELATORIO.md`: tabelas, análise e respostas às perguntas do enunciado.

## Requisitos

- Python 3.10 ou superior (o projeto usa apenas recursos básicos da linguagem e a biblioteca padrão).
- Não é necessário instalar pacotes externos.

## Como executar

Abra o terminal na pasta do projeto.

### Executar o menu de consultas

```bash
python main.py
```

### Executar os testes funcionais

```bash
python testes_funcionais.py
```

Se todos os testes forem aprovados, a última mensagem será `Todos os testes funcionais passaram!`.

### Executar os experimentos

```bash
python experimento1.py
python experimento2.py
```

Os tempos variam conforme o computador e os programas em execução. Para preencher o relatório definitivo, execute os dois experimentos no mesmo computador e registre os resultados obtidos.

## Como funciona o índice

A função `construir_indice(texto)` separa o texto em linhas, começa a numeração em 1, transforma as palavras em letras minúsculas e retira sinais de pontuação. Cada palavra é uma chave do dicionário e seu valor é um conjunto (`set`) com os números das linhas em que aparece.

As funções de consulta retornam listas ordenadas:

- `buscar(indice, palavra)`: linhas em que aparece uma palavra.
- `buscar_e(indice, palavras)`: linhas que contêm todas as palavras (interseção).
- `buscar_ou(indice, palavras)`: linhas que contêm pelo menos uma das palavras (união).

As funções de busca não imprimem resultados, não recebem dados pelo teclado e não modificam o índice recebido.
