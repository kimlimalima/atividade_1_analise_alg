import matplotlib.pyplot as plt
import numpy as np

n = np.arange(1, 100)

n_quadrado_log_n = (n+1)**2

n_quadrado = (n**2)

plt.plot(n, n_quadrado_log_n, label='(n+1)**2', linestyle='-')
plt.plot(n, n_quadrado, label='n^2', linestyle='-.')

plt.xlabel('n')
plt.ylabel('Valor')
plt.title('Comparação entre (n+1)**2 e n^2')

plt.legend()

plt.savefig("Caso 3.jpg", dpi=600)
