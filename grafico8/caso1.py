import matplotlib.pyplot as plt
import numpy as np

n = np.arange(1, 100)

log_n = np.log10(n)

n_cubico = n**3

plt.plot(n, log_n, label='log(n)', linestyle='-', marker='o')
plt.plot(n, n_cubico, label='n^3', linestyle='--', marker='x')

plt.xlabel('n')
plt.ylabel('Valor')
plt.title('Comparação entre log(n) e n^3')

plt.legend()
plt.savefig("Caso 1.jpg", dpi=600)