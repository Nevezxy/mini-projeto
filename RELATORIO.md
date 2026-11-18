# RELATÓRIO — MINI-PROJETO: ÍNDICE INVERTIDO PARA BUSCA TEXTUAL

**Instituição:** Instituto Federal de Alagoas – IFAL / Campus Maceió  
**Curso:** Bacharelado em Sistemas de Informação  
**Disciplina:** Estruturas de Dados  
**Aluno1:** Eduardo Lins Maciel das Neves  
**Aluno2:** Diogo Henrique Barbosa da Silva

---

## 1. INTRODUÇÃO

Neste projeto, desenvolvi um programa em Python que permite pesquisar palavras em um texto e identificar em quais linhas elas aparecem.

Para realizar essa tarefa, utilizei dicionários, conjuntos e listas, construindo um índice invertido que facilita a localização das palavras sem precisar percorrer todo o texto a cada consulta.

O programa possui três tipos de pesquisa: busca simples, busca E e busca OU.

Além disso, desenvolvi uma segunda estratégia de pesquisa, chamada busca por varredura completa, para comparar o desempenho das duas formas de pesquisa.

O objetivo foi compreender como o índice invertido funciona e verificar sua vantagem em relação à busca tradicional.

## 2. DESENVOLVIMENTO DO PROJETO

O projeto foi desenvolvido utilizando Python, com o objetivo de construir um mecanismo simples de busca textual.

Durante o desenvolvimento, foram implementadas as seguintes funcionalidades:

- Separação do texto em linhas, começando a numeração em 1.
- Separação das palavras e conversão para letras minúsculas.
- Remoção de sinais de pontuação.
- Construção de um dicionário contendo as palavras e seus conjuntos de linhas.
- Implementação da busca simples.
- Implementação das buscas E e OU.
- Criação de um menu para permitir que o usuário realize consultas.

Para armazenar as informações, utilizei um dicionário, no qual cada palavra funciona como uma chave e seu valor é um conjunto contendo os números das linhas em que ela aparece.

Também utilizei conjuntos porque eles não permitem elementos repetidos, evitando que uma mesma linha seja armazenada várias vezes para uma palavra.

## 3. TESTES FUNCIONAIS

Foram realizados dez testes funcionais para verificar se o programa estava funcionando corretamente.

Os testes verificaram:

1. Construção correta do índice invertido.
2. Funcionamento da busca simples.
3. Funcionamento da busca E.
4. Funcionamento da busca OU.
5. Funcionamento com texto vazio.
6. Tratamento de palavras repetidas.
7. Contagem correta de linhas vazias.
8. Tratamento de pontuação.
9. Preservação de palavras com e sem acentos.
10. Consultas envolvendo três palavras.

Todos os dez testes funcionais passaram corretamente.

Também foram acrescentados testes durante a revisão do projeto, incluindo verificações adicionais de pontuação e preservação do índice durante as consultas.

## 4. EXPERIMENTO 1 — TEMPO DE BUSCA

### 4.1. Objetivo

O objetivo deste experimento foi comparar o tempo necessário para realizar 1.000 pesquisas utilizando a busca por varredura completa e a busca com índice invertido.

Para isso, utilizei um texto de exemplo repetido 2.000 vezes, aumentando sua quantidade de linhas.

As duas estratégias utilizaram as mesmas palavras nas consultas.

### 4.2. Resultados

| Medição | Tempo (ms) |
|---|---:|
| Construção do índice | 24,667 |
| 1.000 buscas por varredura | 19.327,918 |
| 1.000 buscas com índice | 23,731 |

### 4.3. Análise dos resultados

Os resultados mostraram uma grande diferença de desempenho entre as duas estratégias.

A busca por varredura completa levou aproximadamente 19 segundos para realizar as 1.000 pesquisas.

Já a busca utilizando o índice invertido levou aproximadamente 24 milissegundos.

Mesmo considerando o tempo necessário para construir o índice, que foi de 24,667 ms, a estratégia indexada continuou apresentando um desempenho muito superior.

Somando a construção do índice e as consultas, o tempo total foi de 48,398 ms.

Isso demonstra que o índice invertido pode melhorar bastante o desempenho quando precisamos realizar muitas pesquisas no mesmo texto.

## 5. EXPERIMENTO 2 — VANTAGEM DA INDEXAÇÃO

### 5.1. Objetivo

Neste experimento, procurei descobrir se o tempo necessário para construir o índice invertido é compensado quando realizamos várias consultas.

Para isso, comparei as duas estratégias utilizando diferentes quantidades de pesquisas:

- 1 consulta;
- 10 consultas;
- 100 consultas;
- 1.000 consultas.

Cada medição foi realizada três vezes, utilizando a mediana dos resultados.

### 5.2. Resultados

| Quantidade de consultas | Varredura completa (ms) | Construção + índice (ms) |
|---:|---:|---:|
| 1 | 25,821 | 25,944 |
| 10 | 210,082 | 21,497 |
| 100 | 2.191,430 | 24,930 |
| 1.000 | 21.074,019 | 61,858 |

### 5.3. Análise dos resultados

Com apenas uma consulta, a busca por varredura completa foi ligeiramente mais rápida, apresentando uma diferença muito pequena em relação à indexação.

Com 10 consultas, a busca utilizando o índice invertido já apresentou uma vantagem significativa, sendo aproximadamente 9,77 vezes mais rápida.

Com 100 consultas, a diferença aumentou ainda mais, chegando a aproximadamente 87,90 vezes.

Já com 1.000 consultas, a busca indexada foi aproximadamente 340,70 vezes mais rápida, mesmo considerando o tempo necessário para construir o índice.

Esses resultados mostram que a construção do índice possui um custo inicial, mas esse custo é compensado quando precisamos realizar várias pesquisas no mesmo texto.

## 6. ANÁLISE DOS RESULTADOS — SEIS QUESTÕES

### 1. Qual estratégia foi mais rápida? Em quais situações?

A busca por varredura completa foi ligeiramente mais rápida quando realizei apenas uma consulta.

Porém, quando aumentei a quantidade de pesquisas, a busca utilizando o índice invertido apresentou um desempenho muito melhor.

Isso acontece porque a varredura precisa percorrer o texto inteiro a cada pesquisa, enquanto o índice já possui as palavras organizadas em um dicionário.

### 2. A partir de aproximadamente quantas consultas a indexação passou a ser vantajosa?

Com base nos resultados, a indexação passou a ser vantajosa entre 1 e 10 consultas.

Com uma consulta, a varredura foi um pouco mais rápida. Já com 10 consultas, o índice invertido apresentou uma vantagem significativa.

O ponto de equilíbrio exato não foi medido, mas os resultados indicam que a construção do índice começa a compensar quando precisamos realizar mais de uma pesquisa.

### 3. Qual é a vantagem de utilizar conjuntos em vez de listas para armazenar as linhas?

A principal vantagem dos conjuntos é que eles não permitem elementos repetidos.

Assim, mesmo que uma palavra apareça várias vezes na mesma linha, seu número será armazenado apenas uma vez.

Além disso, os conjuntos facilitam operações como união e interseção, que foram utilizadas nas buscas OU e E.

### 4. Qual é a complexidade esperada da busca de uma chave em um dicionário Python?

A complexidade esperada é O(1), ou seja, tempo constante em média.

Isso acontece porque os dicionários utilizam tabelas hash, permitindo localizar uma chave sem precisar percorrer todas as outras palavras armazenadas.

Em situações desfavoráveis de colisões, o desempenho pode ser pior.

### 5. Qual é a complexidade da construção do índice e das operações de união e interseção?

A construção do índice possui complexidade esperada O(T), considerando T como a quantidade total de caracteres do texto, pois precisamos percorrer o conteúdo para separar as palavras e armazenar suas linhas.

A união de dois conjuntos possui complexidade O(n + m), considerando a quantidade de elementos dos dois conjuntos.

A interseção possui complexidade esperada O(min(n, m)) na implementação usual de conjuntos Python, considerando n e m como os tamanhos dos conjuntos.

Essas operações ajudam a realizar as consultas combinadas de maneira eficiente.

### 6. Qual é a principal desvantagem da indexação em relação ao consumo de memória?

A principal desvantagem é que o índice invertido precisa armazenar informações adicionais na memória.

Além do texto original, precisamos guardar um dicionário com todas as palavras encontradas e os conjuntos contendo os números das linhas em que aparecem.

Quanto maior o texto e a quantidade de palavras diferentes, maior poderá ser o consumo de memória.

## 7. CONCLUSÃO

Com o desenvolvimento deste projeto, consegui compreender melhor como funcionam os dicionários, conjuntos e listas em Python.

Durante os experimentos, percebi que a busca por varredura completa pode funcionar bem quando precisamos realizar poucas pesquisas, mas apresenta um desempenho muito inferior quando a quantidade de consultas aumenta.

Já o índice invertido exige um tempo inicial para ser construído, mas permite realizar pesquisas posteriores de maneira muito mais rápida.

Os resultados obtidos demonstraram essa diferença, principalmente no experimento com 1.000 consultas.

No geral, o projeto foi importante para colocar em prática os conceitos estudados na disciplina de Estruturas de Dados e compreender como diferentes estruturas podem influenciar o desempenho de um programa.