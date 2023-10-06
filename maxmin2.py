import random

"""
No melhor caso o algoritmo só faria a comparação na primeira condicional. Assim seriam (n-1) comparações.

Porém, no pior caso as duas condicionais seriam executadas. Gerando assim 2*(n-1) comparações.

Ficariamos com:
(n-1) comparações no melhor caso
2*(n-1) comparações no pior caso.

Conclusão:
No melhor caso ele teria um número menor de comparações do que o primeiro algorimo.
Porém, no pior caso ele teria o mesmo número de comparações que o maxmin1.
Logo, os algoritmos tem semelhanças no número de comparações dependendo da entrada realizada.
"""

A = [random.randint(1,100) for _ in range(10)]

def max_min_2(A):
    
    Max = Min = A[0]

    for i in range(1, len(A)):
        if A[i] > Max: # # (n – 1) tanto no melhor quanto no pior caso;
            Max = A[i]
        elif A[i] < Min: # (0) no melhor caso e (n-1) no pior caso.
            Min = A[i]

    return Max, Min

maximo, minimo = max_min_2(A)

print(f"Vetor: {A}\n\nMáximo: {maximo}\nMínimo: {minimo}\n\n")
print(f"Vetor: {A}\n\nFunção Max: {max(A)}\nFunção Min: {min(A)}\n")
