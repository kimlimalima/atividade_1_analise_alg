import matplotlib.pyplot as plt
import numpy as np

n = np.arange(1, 100)

log_n = 3*np.log10(n**2)+2

n_cubico = np.log10(n)

plt.plot(n, log_n, label='3*log10(n**2)+2', linestyle='-', marker='o')
plt.plot(n, n_cubico, label='log10(n)', linestyle='--', marker='x')

plt.xlabel('n')
plt.ylabel('Valor')
plt.title('Comparação entre 3*log10(n**2)+2 e log10(n)')

plt.legend()
plt.savefig("parte2.jpg", dpi=600)