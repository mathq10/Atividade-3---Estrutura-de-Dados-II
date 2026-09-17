# Análise dos Resultados

Os resultados apresentados nesta análise foram obtidos através da execução do programa `main.py`.

Foram realizados experimentos com vetores de 10, 20 e 1.000 elementos. Para cada tamanho, os quatro algoritmos receberam exatamente o mesmo vetor inicial, permitindo uma comparação mais justa entre eles.

---

## Resultados dos experimentos

| Tamanho | Bubble Comp. | Bubble Trocas | Insertion Comp. | Insertion Mov. | Selection Comp. | Selection Trocas | Quick Comp. | Quick Mov. |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 10 | 45 | 25 | 31 | 34 | 45 | 7 | 20 | 13 |
| 20 | 190 | 109 | 123 | 128 | 190 | 17 | 76 | 35 |
| 1.000 | 499.500 | 252.209 | 253.199 | 253.208 | 499.500 | 993 | 11.235 | 4.570 |

---

## a) Qual algoritmo realizou o menor número de comparações para 10 elementos?

Para o vetor com 10 elementos, o **Quick Sort** realizou o menor número de comparações, com apenas **20 comparações**.

O Insertion Sort realizou 31 comparações, enquanto Bubble Sort e Selection Sort realizaram 45 comparações cada.

Portanto, nos dados obtidos:

- Quick Sort: **20**
- Insertion Sort: **31**
- Bubble Sort: **45**
- Selection Sort: **45**

---

## b) Qual algoritmo realizou menos trocas ou movimentações?

Para 10 elementos, o **Selection Sort** realizou a menor quantidade de trocas, com apenas **7 trocas**.

Os resultados foram:

- Selection Sort: **7**
- Quick Sort: **13**
- Bubble Sort: **25**
- Insertion Sort: **34 movimentações**

O mesmo comportamento pode ser observado no vetor de 1.000 elementos em relação às trocas/movimentações. O Selection Sort realizou **993 trocas**, enquanto o Bubble Sort realizou **252.209 trocas**, o Insertion Sort realizou **253.208 movimentações** e o Quick Sort realizou **4.570 movimentações**.

---

## c) O comportamento observado para 10 elementos permaneceu semelhante quando o tamanho aumentou para 20?

De maneira geral, sim. O comportamento observado para 10 elementos continuou semelhante para 20 elementos.

O Quick Sort continuou apresentando a menor quantidade de comparações:

- 10 elementos: **20 comparações**
- 20 elementos: **76 comparações**

O Bubble Sort e o Selection Sort também continuaram apresentando a mesma quantidade de comparações:

- 10 elementos: **45**
- 20 elementos: **190**

O Insertion Sort apresentou crescimento de 31 para 123 comparações.

Portanto, mesmo com o aumento do vetor, os padrões observados inicialmente continuaram presentes.

---

## d) O que aconteceu com a quantidade de operações quando o vetor passou para 1.000 elementos?

Quando o vetor passou de 20 para 1.000 elementos, houve um aumento muito grande na quantidade de operações, principalmente nos algoritmos com comportamento quadrático.

O Bubble Sort passou de **190 para 499.500 comparações** e realizou **252.209 trocas**.

O Selection Sort passou de **190 para 499.500 comparações**, realizando **993 trocas**.

O Insertion Sort passou de **123 para 253.199 comparações** e realizou **253.208 movimentações**.

Já o Quick Sort passou de **76 para 11.235 comparações** e realizou **4.570 movimentações**.

A diferença mostra que o aumento do tamanho do vetor torna mais evidente o comportamento de cada algoritmo.

---

## e) Bubble Sort, Insertion Sort e Selection Sort apresentam complexidade O(n²) em situações típicas estudadas. Eles apresentaram exatamente a mesma quantidade de operações?

Não. Apesar de Bubble Sort, Insertion Sort e Selection Sort apresentarem comportamento O(n²) em situações típicas estudadas, eles não realizaram exatamente a mesma quantidade de operações.

Por exemplo, para 1.000 elementos:

- Bubble Sort realizou **499.500 comparações** e **252.209 trocas**;
- Insertion Sort realizou **253.199 comparações** e **253.208 movimentações**;
- Selection Sort realizou **499.500 comparações** e apenas **993 trocas**.

Isso mostra que a complexidade assintótica não determina a quantidade exata de operações realizadas.

Ela representa principalmente como o número de operações cresce conforme o tamanho da entrada aumenta.

Além disso, cada algoritmo possui uma estratégia diferente para ordenar os elementos, fazendo com que a quantidade de comparações, trocas e movimentações seja diferente.

---

## f) Qual algoritmo apresentou maior crescimento no número de operações?

Considerando o total de operações, o **Bubble Sort apresentou o maior crescimento** entre os resultados obtidos.

Para 1.000 elementos, o Bubble Sort realizou:

- **499.500 comparações**
- **252.209 trocas**

Totalizando **751.709 operações contabilizadas**.

O Selection Sort realizou 499.500 comparações e 993 trocas, totalizando 500.493 operações.

O Insertion Sort realizou 253.199 comparações e 253.208 movimentações, totalizando 506.407 operações.

O Quick Sort realizou 11.235 comparações e 4.570 movimentações, totalizando 15.805 operações.

Portanto, considerando a soma das operações contabilizadas, o Bubble Sort apresentou o maior crescimento no experimento.

---

## g) Como o comportamento experimental do Quick Sort se diferenciou dos demais algoritmos?

O Quick Sort apresentou uma quantidade de operações significativamente menor nos vetores aleatórios utilizados nos experimentos.

Para 1.000 elementos, foram realizadas:

- **11.235 comparações**
- **4.570 movimentações**

Enquanto o Bubble Sort e o Selection Sort realizaram **499.500 comparações** cada.

Essa diferença está relacionada à estratégia de divisão e conquista utilizada pelo Quick Sort.

Nos resultados obtidos, o crescimento do Quick Sort foi muito menor que o observado nos algoritmos quadráticos.

---

## h) Os resultados encontrados são coerentes com as complexidades teóricas estudadas?

Sim. Os resultados encontrados são coerentes com as complexidades teóricas estudadas.

Bubble Sort e Selection Sort apresentaram **499.500 comparações** para 1.000 elementos, demonstrando o crescimento quadrático esperado.

O Insertion Sort também apresentou um crescimento elevado, chegando a **253.199 comparações** para 1.000 elementos.

Já o Quick Sort apresentou **11.235 comparações** para 1.000 elementos, um crescimento consideravelmente menor nos dados utilizados.

Esses resultados são compatíveis com a complexidade média teórica do Quick Sort, que é `O(n log n)`, enquanto Bubble Sort, Insertion Sort e Selection Sort apresentam comportamento `O(n²)` em situações típicas estudadas.

É importante destacar que o resultado exato do Quick Sort depende da organização dos dados e da estratégia utilizada para escolha do pivô.

---

## i) Se você fosse responsável pelo sistema da central de distribuição e precisasse ordenar milhares de pedidos, qual dos quatro algoritmos escolheria?

Com base nos resultados deste experimento, eu escolheria o **Quick Sort** para uma situação com milhares de pedidos.

Para 1.000 elementos, o Quick Sort realizou:

- **11.235 comparações**
- **4.570 movimentações**

Enquanto:

- Bubble Sort realizou 499.500 comparações;
- Selection Sort realizou 499.500 comparações;
- Insertion Sort realizou 253.199 comparações.

A diferença aumenta conforme a quantidade de elementos cresce. Portanto, para grandes quantidades de pedidos, os resultados experimentais indicam que o Quick Sort apresenta um comportamento mais adequado entre os quatro algoritmos analisados.

---

# Desafio Adicional

No desafio adicional, foram utilizados vetores com 100 elementos em três situações diferentes:

1. Vetor aleatório;
2. Vetor já ordenado;
3. Vetor em ordem inversa.

---

## Vetor aleatório

| Algoritmo | Comparações | Trocas/Movimentações |
|---|---:|---:|
| Bubble Sort | 4.950 | 2.566 |
| Insertion Sort | 2.662 | 2.665 |
| Selection Sort | 4.950 | 96 |
| Quick Sort | 587 | 238 |

No vetor aleatório, o Quick Sort apresentou a menor quantidade de comparações e movimentações.

O Selection Sort, apesar de realizar 4.950 comparações, realizou apenas 96 trocas.

---

## Vetor já ordenado

| Algoritmo | Comparações | Trocas/Movimentações |
|---|---:|---:|
| Bubble Sort | 4.950 | 0 |
| Insertion Sort | 99 | 99 |
| Selection Sort | 4.950 | 0 |
| Quick Sort | 4.950 | 0 |

No vetor já ordenado, o Insertion Sort apresentou uma grande redução na quantidade de comparações, realizando apenas 99.

Já o Bubble Sort, Selection Sort e Quick Sort realizaram 4.950 comparações cada.

Isso mostra que a organização inicial dos dados pode ter grande influência no comportamento de determinados algoritmos.

---

## Vetor em ordem inversa

| Algoritmo | Comparações | Trocas/Movimentações |
|---|---:|---:|
| Bubble Sort | 4.950 | 4.950 |
| Insertion Sort | 4.950 | 5.049 |
| Selection Sort | 4.950 | 50 |
| Quick Sort | 4.950 | 50 |

No vetor em ordem inversa, Bubble Sort e Insertion Sort apresentaram uma quantidade elevada de movimentações.

O Selection Sort e o Quick Sort realizaram apenas 50 movimentações de acordo com o critério de contagem utilizado no programa.

---

## A organização inicial dos dados interfere na quantidade de operações realizadas por todos os algoritmos da mesma maneira?

Não. A organização inicial dos dados não interfere da mesma maneira em todos os algoritmos.

Isso pode ser observado principalmente no Insertion Sort. Com o vetor já ordenado, ele realizou apenas **99 comparações e 99 movimentações**. Já com o vetor em ordem inversa, realizou **4.950 comparações e 5.049 movimentações**.

O Bubble Sort realizou 4.950 comparações tanto no vetor aleatório, quanto no vetor ordenado e no vetor inverso. Porém, a quantidade de trocas variou bastante:

- Aleatório: **2.566**
- Ordenado: **0**
- Inverso: **4.950**

O Selection Sort também manteve 4.950 comparações nos três casos, mas apresentou diferenças nas trocas.

No Quick Sort, a organização inicial também teve influência. No vetor aleatório foram realizadas **587 comparações**, enquanto nos vetores ordenado e inverso foram realizadas **4.950 comparações**.

Isso ocorre porque a implementação utilizada escolhe o último elemento do trecho como pivô. Dependendo da organização do vetor, essa escolha pode produzir partições menos equilibradas.

---

# Conclusão

O experimento permitiu analisar na prática o comportamento dos algoritmos Bubble Sort, Insertion Sort, Selection Sort e Quick Sort.

Os resultados mostraram que algoritmos com comportamento O(n²) podem apresentar quantidades diferentes de operações, mesmo possuindo a mesma ordem de complexidade.

Com 1.000 elementos, a diferença ficou bastante evidente. O Bubble Sort realizou **499.500 comparações e 252.209 trocas**, enquanto o Quick Sort realizou **11.235 comparações e 4.570 movimentações**.

O desafio adicional também demonstrou que a organização inicial dos dados pode alterar significativamente a quantidade de operações realizadas. O Insertion Sort, por exemplo, apresentou apenas 99 comparações no vetor já ordenado, enquanto chegou a 4.950 comparações no vetor em ordem inversa.

Dessa forma, o experimento permitiu relacionar os conceitos teóricos de complexidade de algoritmos com resultados obtidos na prática, mostrando como a escolha do algoritmo pode influenciar o desempenho de um sistema quando a quantidade de dados aumenta.