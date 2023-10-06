import matplotlib.pyplot as plt
import numpy as np

n = np.arange(1, 100)

n_quadrado_log_n = n**2*(np.log10(n))

n_quadrado = n**2

plt.plot(n, n_quadrado_log_n, label='n^2log(n)', linestyle='-', marker='o')
plt.plot(n, n_quadrado, label='n^2', linestyle='--', marker='x')

plt.xlabel('n')
plt.ylabel('Valor')
plt.title('Comparação entre n^2log(n) e n^2')

plt.legend()

plt.savefig("Caso 2.jpg", dpi=600)
