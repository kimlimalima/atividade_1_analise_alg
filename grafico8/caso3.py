import matplotlib.pyplot as plt
import numpy as np

n = np.arange(1, 100)

n_quadrado = n**2

n_quadrado_log_n = n**2*(np.log10(n))

plt.plot(n, n_quadrado, label='n^2', linestyle='-', marker='o')
plt.plot(n, n_quadrado_log_n, label='n^2log(n)', linestyle='--', marker='x')

plt.xlabel('n')
plt.ylabel('Valor')
plt.title('Comparação entre n^2 e n^2log(n)')

plt.legend()

plt.savefig("Caso 3.jpg", dpi=600)
