# RELATÓRIO — MINI-PROJETO: ÍNDICE INVERTIDO PARA BUSCA TEXTUAL

**Instituição:** Instituto Federal de Alagoas – IFAL / Campus Maceió  
**Curso:** Bacharelado em Sistemas de Informação  
**Disciplina:** Estruturas de Dados  
**Aluno 1:** Eduardo Lins Maciel das Neves  
**Aluno 2:** Diogo Henrique Barbosa da Silva  
**Data:** 17/11/2026

---

## 1. INTRODUÇÃO

Neste projeto, desenvolvi um programa em Python que permite pesquisar palavras em um texto e identificar em quais linhas elas aparecem.

Para realizar essa tarefa, utilizei dicionários, conjuntos e listas, construindo um índice invertido que facilita a localização das palavras sem precisar percorrer todo o texto a cada consulta.

O programa possui três tipos de pesquisa: busca simples, busca E e busca OU. Também foi desenvolvida uma busca por varredura completa para comparar o desempenho das duas estratégias.

## 2. DESENVOLVIMENTO DO PROJETO

O projeto foi desenvolvido utilizando Python. Foram implementadas a separação do texto em linhas, a normalização das palavras, a remoção de pontuação, a construção do índice invertido e as três modalidades de consulta.

O índice é um dicionário no qual cada palavra funciona como chave e seu valor é um conjunto com os números das linhas em que ela aparece. Os conjuntos evitam números de linha repetidos e permitem realizar operações de união e interseção.

## 3. TESTES FUNCIONAIS

O arquivo `testes_funcionais.py` contém **12 testes funcionais**. Eles verificam a construção do índice, busca simples, busca E, busca OU, texto vazio, palavras repetidas, linhas vazias, pontuação, acentos, consultas com três palavras, pontuação adicional e preservação do índice após consultas.

Na versão publicada no repositório, os testes são executados com:

```bash
python testes_funcionais.py
```

Registre aqui o resultado da execução final feita antes da entrega. Não declare que os testes passaram se não tiver executado a versão final dos arquivos.

## 4. EXPERIMENTO 1 — TEMPO DE BUSCA

### 4.1. Objetivo

Comparar 1.000 pesquisas por varredura completa e 1.000 pesquisas utilizando o índice invertido.

### 4.2. Resultados medidos

| Medição | Tempo (ms) |
|---|---:|
| Construção do índice | 24,667 |
| 1.000 buscas por varredura | 19.327,918 |
| 1.000 buscas com índice | 23,731 |

Somando a construção do índice e as consultas, a estratégia indexada levou 48,398 ms.

### 4.3. Análise

A varredura completa levou aproximadamente 19,3 segundos para realizar as 1.000 pesquisas. A busca utilizando o índice levou aproximadamente 23,7 milissegundos. Mesmo incluindo a construção do índice, a estratégia indexada foi muito mais rápida nesse cenário.

## 5. EXPERIMENTO 2 — VANTAGEM DA INDEXAÇÃO

### 5.1. Objetivo

Comparar as estratégias com 1, 10, 100 e 1.000 consultas. Segundo o registro do experimento, cada quantidade foi medida três vezes e foi utilizada a mediana.

### 5.2. Resultados medidos

| Quantidade de consultas | Varredura completa (ms) | Construção + índice (ms) |
|---:|---:|---:|
| 1 | 25,821 | 25,944 |
| 10 | 210,082 | 21,497 |
| 100 | 2.191,430 | 24,930 |
| 1.000 | 21.074,019 | 61,858 |

### 5.3. Análise

Com uma consulta, a varredura foi ligeiramente mais rápida: a diferença foi de apenas 0,123 ms. Com 10 consultas, o tempo da varredura foi aproximadamente 9,77 vezes maior. Com 100 consultas, foi aproximadamente 87,90 vezes maior. Com 1.000 consultas, foi aproximadamente 340,70 vezes maior.

Os resultados mostram que o índice tem um custo inicial de construção, mas esse custo é compensado quando várias consultas são realizadas sobre o mesmo texto.

## 6. ANÁLISE DOS RESULTADOS — SEIS QUESTÕES

### 1. Qual estratégia foi mais rápida? Em quais situações?

A varredura completa foi ligeiramente mais rápida quando realizei apenas uma consulta. Quando a quantidade de pesquisas aumentou, a busca utilizando o índice invertido apresentou um desempenho muito melhor. Isso acontece porque a varredura precisa percorrer o texto a cada pesquisa, enquanto o índice já possui as palavras organizadas em um dicionário.

### 2. A partir de aproximadamente quantas consultas a indexação passou a ser vantajosa?

Com base nos resultados, a vantagem já aparece no teste de 10 consultas. Com uma consulta, a varredura foi um pouco mais rápida. O ponto de equilíbrio exato não foi medido; sabemos apenas que, neste experimento, ele está entre 1 e 10 consultas.

### 3. Qual é a vantagem de utilizar conjuntos em vez de listas para armazenar as linhas?

Os conjuntos não permitem elementos repetidos. Assim, mesmo que uma palavra apareça várias vezes na mesma linha, seu número será armazenado apenas uma vez. Além disso, conjuntos facilitam operações de união e interseção, utilizadas nas buscas OU e E.

### 4. Qual é a complexidade esperada da busca de uma chave em um dicionário Python?

A complexidade esperada é O(1), ou seja, tempo constante em média, porque os dicionários utilizam tabelas hash. Em situações desfavoráveis de colisões, o desempenho pode ser pior.

### 5. Qual é a complexidade da construção do índice e das operações de união e interseção?

Considerando T como a quantidade total de caracteres do texto, a construção percorre o texto para separar e armazenar as palavras, tendo custo esperado linear em relação ao tamanho da entrada, além do custo das operações de conjuntos.

A união de conjuntos de tamanhos n e m possui custo O(n + m). A interseção, na implementação usual, tem custo proporcional ao menor conjunto quando a operação percorre o menor conjunto e verifica os elementos no maior, com busca média constante.

### 6. Qual é a principal desvantagem da indexação em relação ao consumo de memória?

A principal desvantagem é o consumo adicional de memória. Além do texto original, é necessário armazenar o dicionário, as palavras e os conjuntos com os números das linhas em que aparecem. Quanto maior o texto e a quantidade de palavras diferentes, maior pode ser esse consumo.

## 7. CONCLUSÃO

Com o desenvolvimento deste projeto, consegui compreender melhor como funcionam os dicionários, conjuntos e listas em Python.

Os experimentos mostraram que a busca por varredura completa pode funcionar bem quando precisamos realizar poucas pesquisas, mas apresenta desempenho inferior quando a quantidade de consultas aumenta. O índice invertido exige um tempo inicial para ser construído, mas permite realizar pesquisas posteriores de maneira muito mais rápida.

O projeto foi importante para colocar em prática os conceitos estudados na disciplina de Estruturas de Dados e compreender como diferentes estruturas podem influenciar o desempenho de um programa.
