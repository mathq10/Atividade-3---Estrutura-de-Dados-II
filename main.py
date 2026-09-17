import random


# ============================================================
# BUBBLE SORT
# ============================================================

def bubble_sort(vetor):
    vetor = vetor.copy()
    comparacoes = 0
    trocas = 0

    n = len(vetor)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            comparacoes += 1

            if vetor[j] > vetor[j + 1]:
                vetor[j], vetor[j + 1] = vetor[j + 1], vetor[j]
                trocas += 1

    return vetor, comparacoes, trocas


# ============================================================
# INSERTION SORT
# ============================================================

def insertion_sort(vetor):
    vetor = vetor.copy()
    comparacoes = 0
    movimentacoes = 0

    for i in range(1, len(vetor)):
        chave = vetor[i]
        j = i - 1

        while j >= 0:
            comparacoes += 1

            if vetor[j] > chave:
                vetor[j + 1] = vetor[j]
                movimentacoes += 1
                j -= 1
            else:
                break

        vetor[j + 1] = chave
        movimentacoes += 1

    return vetor, comparacoes, movimentacoes


# ============================================================
# SELECTION SORT
# ============================================================

def selection_sort(vetor):
    vetor = vetor.copy()
    comparacoes = 0
    trocas = 0

    n = len(vetor)

    for i in range(n - 1):
        menor = i

        for j in range(i + 1, n):
            comparacoes += 1

            if vetor[j] < vetor[menor]:
                menor = j

        if menor != i:
            vetor[i], vetor[menor] = vetor[menor], vetor[i]
            trocas += 1

    return vetor, comparacoes, trocas


# ============================================================
# QUICK SORT
# ============================================================

def quick_sort(vetor):
    vetor = vetor.copy()
    comparacoes = 0
    movimentacoes = 0

    def ordenar(inicio, fim):
        nonlocal comparacoes, movimentacoes

        if inicio < fim:
            pivo = vetor[fim]
            i = inicio - 1

            for j in range(inicio, fim):
                comparacoes += 1

                if vetor[j] <= pivo:
                    i += 1

                    if i != j:
                        vetor[i], vetor[j] = vetor[j], vetor[i]
                        movimentacoes += 1

            if i + 1 != fim:
                vetor[i + 1], vetor[fim] = vetor[fim], vetor[i + 1]
                movimentacoes += 1

            posicao_pivo = i + 1

            ordenar(inicio, posicao_pivo - 1)
            ordenar(posicao_pivo + 1, fim)

    ordenar(0, len(vetor) - 1)

    return vetor, comparacoes, movimentacoes


# ============================================================
# EXPERIMENTO
# ============================================================

def executar_experimento(tamanho):
    # Gera um único vetor original
    vetor_original = [random.randint(1, 10000) for _ in range(tamanho)]

    # Cria cópias idênticas para cada algoritmo
    vetor_bubble = vetor_original.copy()
    vetor_insertion = vetor_original.copy()
    vetor_selection = vetor_original.copy()
    vetor_quick = vetor_original.copy()

    # Executa os algoritmos
    _, bubble_comp, bubble_trocas = bubble_sort(vetor_bubble)

    _, insertion_comp, insertion_mov = insertion_sort(vetor_insertion)

    _, selection_comp, selection_trocas = selection_sort(vetor_selection)

    _, quick_comp, quick_mov = quick_sort(vetor_quick)

    return {
        "Tamanho": tamanho,
        "Bubble Comparações": bubble_comp,
        "Bubble Trocas": bubble_trocas,
        "Insertion Comparações": insertion_comp,
        "Insertion Mov.": insertion_mov,
        "Selection Comparações": selection_comp,
        "Selection Trocas": selection_trocas,
        "Quick Comparações": quick_comp,
        "Quick Mov.": quick_mov
    }


# ============================================================
# DESAFIO ADICIONAL
# ============================================================

def executar_desafio(vetor, nome):

    print("\n" + "=" * 80)
    print("DESAFIO -", nome)
    print("=" * 80)

    _, bubble_comp, bubble_trocas = bubble_sort(vetor)
    _, insertion_comp, insertion_mov = insertion_sort(vetor)
    _, selection_comp, selection_trocas = selection_sort(vetor)
    _, quick_comp, quick_mov = quick_sort(vetor)

    print(f"\n{'Algoritmo':<15} {'Comparações':<15} {'Trocas/Mov.':<15}")
    print("-" * 50)

    print(f"{'Bubble':<15} {bubble_comp:<15} {bubble_trocas:<15}")
    print(f"{'Insertion':<15} {insertion_comp:<15} {insertion_mov:<15}")
    print(f"{'Selection':<15} {selection_comp:<15} {selection_trocas:<15}")
    print(f"{'Quick':<15} {quick_comp:<15} {quick_mov:<15}")


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

def main():

    print("=" * 100)
    print("ANÁLISE DE ALGORITMOS DE ORDENAÇÃO")
    print("=" * 100)

    tamanhos = [10, 20, 1000]

    resultados = []

    for tamanho in tamanhos:
        resultado = executar_experimento(tamanho)
        resultados.append(resultado)

    # Tabela principal
    print("\n")
    print("=" * 130)
    print("RESULTADOS DOS EXPERIMENTOS")
    print("=" * 130)

    cabecalho = (
        f"{'Tam.':<8}"
        f"{'Bubble C.':<13}"
        f"{'Bubble T.':<13}"
        f"{'Insert C.':<13}"
        f"{'Insert M.':<13}"
        f"{'Select C.':<13}"
        f"{'Select T.':<13}"
        f"{'Quick C.':<13}"
        f"{'Quick M.':<13}"
    )

    print(cabecalho)
    print("-" * 130)

    for r in resultados:
        print(
            f"{r['Tamanho']:<8}"
            f"{r['Bubble Comparações']:<13}"
            f"{r['Bubble Trocas']:<13}"
            f"{r['Insertion Comparações']:<13}"
            f"{r['Insertion Mov.']:<13}"
            f"{r['Selection Comparações']:<13}"
            f"{r['Selection Trocas']:<13}"
            f"{r['Quick Comparações']:<13}"
            f"{r['Quick Mov.']:<13}"
        )

    # ========================================================
    # DESAFIO ADICIONAL
    # ========================================================

    tamanho_desafio = 100

    vetor_aleatorio = [
        random.randint(1, 10000)
        for _ in range(tamanho_desafio)
    ]

    vetor_ordenado = sorted(vetor_aleatorio)

    vetor_inverso = sorted(vetor_aleatorio, reverse=True)

    executar_desafio(vetor_aleatorio, "VETOR ALEATÓRIO")

    executar_desafio(vetor_ordenado, "VETOR JÁ ORDENADO")

    executar_desafio(vetor_inverso, "VETOR EM ORDEM INVERSA")


# Executa o programa
if __name__ == "__main__":
    main()