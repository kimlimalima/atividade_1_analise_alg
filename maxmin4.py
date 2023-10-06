import random

"""
A condião principal será executada (n/2) vezes, até que a comparação seja TRUE.
Uma vez que o quando a CONDIÇÃO PRINCIPAL for TRUE a execução será finzalida.

Enquanto for executada a chamada recursiva da função max_min_4. será realizada a comparação da CONDIÇÃO PRINCIPAL.
Porém quando a CONDIÇÃO PRINCIPAL for TRUE a chamada recursiva não ocorrerá novamente e isso não irá chamar as condicionais abaixo.

Isso fará com que a chamada recursiva executará (n/2)-1 comparações para atribuição dos valores Max e Min.
Levando em consideração que, quando a CONDIÇÃO PRINCIPAL for TRUE os blocos de condicionais relativos a atribuição de Max e Min,
não serão executados. Os mesmos possuiram um numero (n/2)-1 de comparações.

Conclusão
O algortimo possuirá um número de (3n/2)-2 comparações o que o torna melhor do que todos os anteriores no melhor e no pior caso.
"""

A = [random.randint(1,100) for _ in range(10)]

def max_min_4(Linf, Lsup, A):
    if Lsup - Linf <= 1: # CONDIÇÃO PRINCIPAL - (n/2) Será executado quando a CONDIÇÃO PRINCIPAL for TRUE
        if A[Linf] < A[Lsup]: # 1
            return A[Lsup], A[Linf]
        else:
            return A[Linf], A[Lsup]

    Meio = (Linf + Lsup) // 2
    Max1, Min1 = max_min_4(Linf, Meio, A) 
    Max2, Min2 = max_min_4(Meio + 1, Lsup, A)

    Max = Max1 if Max1 > Max2 else Max2 # (n/2)-1 Enquanto a CONDIÇÃO PRINCIPAL for falsa esta será executada.
    Min = Min1 if Min1 < Min2 else Min2 # (n/2)-1 Enquanto a CONDIÇÃO PRINCIPAL for falsa esta será executada.

    return Max, Min

maximo, minimo = max_min_4(0, len(A) - 1, A)
print(f"Vetor: {A}\n\nMáximo: {maximo}\nMínimo: {minimo}\n\n")
print(f"Vetor: {A}\n\nFunção Max: {max(A)}\nFunção Min: {min(A)}\n")
