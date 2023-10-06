import matplotlib.pyplot as plt
import numpy as np

n = np.arange(1, 100)

log_n = n**2*(np.log10(n))

n_cubed = n**2

plt.plot(n, log_n, label='n^2log(n)', linestyle='-', marker='o')
plt.plot(n, n_cubed, label='n^2', linestyle='--', marker='x')

plt.xlabel('n')
plt.ylabel('Valor')
plt.title('Comparação entre log(n) e n^3')

plt.legend()

plt.show()
