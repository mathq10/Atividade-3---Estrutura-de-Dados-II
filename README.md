# Atividade-3---Estrutura-de-Dados-II
# Análise de Algoritmos de Ordenação

## Central de Distribuição de Pedidos

Este projeto apresenta um experimento computacional para analisar e comparar quatro algoritmos de ordenação:

* **Bubble Sort**
* **Insertion Sort**
* **Selection Sort**
* **Quick Sort**

A situação utilizada como base é uma central de distribuição que recebe diversos pedidos com códigos numéricos de prioridade. Esses códigos precisam ser organizados do menor para o maior antes de serem encaminhados para separação e expedição.

O objetivo do experimento é observar como a quantidade de operações realizadas por cada algoritmo se comporta conforme aumenta a quantidade de elementos do vetor.

---

## Objetivos

O experimento tem como objetivos:

* Implementar quatro algoritmos de ordenação em Python;
* Utilizar os mesmos dados iniciais para todos os algoritmos;
* Contabilizar o número de comparações realizadas;
* Contabilizar o número de trocas ou movimentações;
* Comparar os resultados para diferentes tamanhos de vetor;
* Relacionar os resultados experimentais com as complexidades teóricas dos algoritmos.

---

## Algoritmos utilizados

### Bubble Sort

O Bubble Sort percorre o vetor comparando elementos vizinhos. Quando dois elementos estão na ordem incorreta, eles são trocados.

**Complexidade típica:** `O(n²)`

### Insertion Sort

O Insertion Sort organiza os elementos um por vez, inserindo cada novo elemento na posição correta em relação aos elementos anteriores.

Sua complexidade pode variar de acordo com a organização inicial dos dados, sendo `O(n²)` em situações desfavoráveis.

### Selection Sort

O Selection Sort procura o menor elemento da parte ainda não ordenada e o coloca na posição correta.

**Complexidade típica:** `O(n²)`

### Quick Sort

O Quick Sort utiliza a estratégia de divisão e conquista. Um elemento é escolhido como pivô e o vetor é dividido em partes menores, que são ordenadas recursivamente.

**Complexidade média:** `O(n log n)`

**Pior caso:** `O(n²)`

---

## Metodologia

Foram utilizados vetores com:

* **10 elementos**
* **20 elementos**
* **1.000 elementos**

Para cada tamanho, foi gerado um único vetor contendo números aleatórios.

Depois, foram criadas quatro cópias desse mesmo vetor:

```python
vetor_bubble = vetor_original.copy()
vetor_insertion = vetor_original.copy()
vetor_selection = vetor_original.copy()
vetor_quick = vetor_original.copy()
```

Dessa forma, todos os algoritmos recebem exatamente os mesmos dados iniciais em cada experimento, permitindo uma comparação mais justa entre eles.

---

## Critérios de Contagem

### Comparações

Foi considerada como comparação cada operação utilizada para verificar a relação entre dois valores durante o processo de ordenação.

### Bubble Sort

Cada troca de dois elementos foi contabilizada como **1 troca**.

### Insertion Sort

Cada deslocamento de um elemento para abrir espaço foi contabilizado como **1 movimentação**.

A inserção da chave na posição final também foi contabilizada como **1 movimentação**.

### Selection Sort

Cada troca realizada para colocar o menor elemento na posição correta foi contabilizada como **1 troca**.

### Quick Sort

Cada troca entre elementos durante o particionamento foi contabilizada como **1 movimentação**.

---

## Experimentos

O programa realiza os experimentos automaticamente para os três tamanhos definidos:

```text
10 elementos
20 elementos
1.000 elementos
```

Ao final, é exibida uma tabela contendo:

| Algoritmo      | Comparações | Trocas/Movimentações |
| -------------- | ----------: | -------------------: |
| Bubble Sort    |           ✓ |                    ✓ |
| Insertion Sort |           ✓ |                    ✓ |
| Selection Sort |           ✓ |                    ✓ |
| Quick Sort     |           ✓ |                    ✓ |

Os resultados são gerados automaticamente pelo programa e podem variar entre as execuções devido à geração dos números aleatórios.

---

## Desafio Adicional

Também foi realizado um experimento considerando três organizações iniciais dos dados:

1. **Vetor aleatório**
2. **Vetor já ordenado**
3. **Vetor em ordem inversa**

O objetivo é verificar se a organização inicial dos dados interfere na quantidade de operações realizadas pelos algoritmos.

Os resultados permitem observar como cada algoritmo se comporta diante de diferentes condições de entrada.

---

## Estrutura do Projeto

```text
analise-algoritmos-ordenacao/
│
├── main.py
│
├── README.md
│
├── resultados/
│   └── resultados.txt
│
└── docs/
    └── analise.md
```

---

## Como Executar

É necessário ter o **Python 3** instalado.

Após clonar o repositório, entre na pasta do projeto:

```bash
cd analise-algoritmos-ordenacao
```

Execute o programa com:

```bash
python main.py
```

No Windows, caso necessário:

```bash
py main.py
```

Após a execução, os resultados dos experimentos serão exibidos no terminal.

---

## Resultados

Os resultados obtidos nos experimentos são registrados no arquivo:

```text
resultados/resultados.txt
```

A análise detalhada dos resultados e as respostas das questões propostas na atividade estão disponíveis em:

```text
docs/analise.md
```

---

## Conclusão

O experimento permite observar na prática as diferenças entre os algoritmos de ordenação.

Mesmo que Bubble Sort, Insertion Sort e Selection Sort apresentem complexidade `O(n²)` em determinadas situações, isso não significa que eles realizem exatamente a mesma quantidade de operações. A quantidade de comparações, trocas e movimentações depende da implementação e da organização dos dados.

O Quick Sort apresenta comportamento diferente principalmente quando o número de elementos aumenta, devido à sua complexidade média `O(n log n)`.

Dessa forma, o experimento permite relacionar os resultados obtidos na prática com os conceitos de complexidade de algoritmos estudados em teoria.

---

## Tecnologias Utilizadas

* **Python 3**
* **Git**
* **GitHub**

---

## Autores

**Matheus Queirós de Sousa Araújo Carvalho**














1.000





















Etapa 4 – Análise dos resultados
Com base nos valores obtidos pelo seu programa, responda:

a) Qual algoritmo realizou o menor número de comparações para 10 elementos?

b) Qual algoritmo realizou menos trocas ou movimentações?

c) O comportamento observado para 10 elementos permaneceu semelhante quando o tamanho aumentou para 20?

d) O que aconteceu com a quantidade de operações quando o vetor passou para 1.000 elementos?

e) Bubble Sort, Insertion Sort e Selection Sort apresentam complexidade ﻿O parêntese esquerdo n ao quadrado parêntese direito﻿ em situações típicas estudadas. Eles apresentaram exatamente a mesma quantidade de operações? Explique utilizando seus resultados.

f) Qual algoritmo apresentou maior crescimento no número de operações?

g) Como o comportamento experimental do Quick Sort se diferenciou dos demais algoritmos?

h) Os resultados encontrados são coerentes com as complexidades teóricas estudadas?

i) Se você fosse responsável pelo sistema da central de distribuição e precisasse ordenar milhares de pedidos, qual dos quatro algoritmos escolheria? Justifique utilizando os resultados do experimento.





Desafio adicional (0,5)
Repita o experimento utilizando:

um vetor com números aleatórios;
um vetor já ordenado;
um vetor em ordem inversa.
Compare os resultados e analise:

A organização inicial dos dados interfere na quantidade de operações realizadas por todos os algoritmos da mesma maneira?





Entrega - link github
