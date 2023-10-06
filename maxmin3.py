import random

"""
Este algoritmo possui um número de 3n/2-2 comparações em todos os casos possíveis.
Já que as comparações analisada sempre serão executadas independente da entrada.

Tanto no melhor quanto no pior caso existirá um número de (3n/2)-2 comparações.

Conclusão:
Independente da entrada existirá o mesmo número de comparações.
"""

A = [random.randint(1,100) for _ in range(10)]

def max_min_3(A):
    tamanho_vetor = len(A)

    if tamanho_vetor % 2 == 0:
        ultimo_elemento = tamanho_vetor - 1
    else:
        A.append(A[tamanho_vetor - 1])
        ultimo_elemento = tamanho_vetor
        

    if A[0] > A[1]: # 1 comparação
        maximo, minimo = A[0], A[1]
    else:
        maximo, minimo = A[1], A[0]

    for i in range(2, ultimo_elemento, 2):
        if A[i] > A[i + 1]: # CONDIÇÃO PRINCIPAL (n/2)-1 comparações - Sempre será executada
            if A[i] > maximo: # (n/2)-1 comparações - Será executado quando a CONDIÇÃO PRINCIPAL for TRUE
                maximo = A[i]
            if A[i + 1] < minimo: # (n/2)-1 comparações - Será executado quando a CONDIÇÃO PRINCIPAL for TRUE
                minimo = A[i + 1]
        else:
            if A[i] < minimo: # (n/2)-1 comparações - Será executado quando a CONDIÇÃO PRINCIPAL for FALSE
                minimo = A[i]
            if A[i + 1] > maximo: # (n/2)-1 comparações - Será executado quando a CONDIÇÃO PRINCIPAL for FALSE
                maximo = A[i + 1]

    return maximo, minimo

maximo, minimo = max_min_3(A)

print(f"Vetor: {A}\n\nMáximo: {maximo}\nMínimo: {minimo}\n\n")
print(f"Vetor: {A}\n\nFunção Max: {max(A)}\nFunção Min: {min(A)}\n")