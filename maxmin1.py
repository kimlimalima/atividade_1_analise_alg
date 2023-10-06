import random

"""
Resultado é um total de 2*(n-1) comparações.

Conclusão:
Isso se emprega tanto no melhor, quanto no pior caso.
Em todas as situações o algoritmo terá o desempenho de 2*(n-1)

"""

A = [random.randint(1,100) for _ in range(10)]

def max_min_1(A):
    
    Max = Min = A[0]

    for i in range(1, len(A)):
        if A[i] > Max: # n-1 comparações
            Max = A[i]
        if A[i] < Min: # n-1 comparações
            Min = A[i]

    return Max, Min

maximo, minimo = max_min_1(A)

print(f"Vetor: {A}\n\nMáximo: {maximo}\nMínimo: {minimo}\n\n")
print(f"Vetor: {A}\n\nFunção Max: {max(A)}\nFunção Min: {min(A)}\n")