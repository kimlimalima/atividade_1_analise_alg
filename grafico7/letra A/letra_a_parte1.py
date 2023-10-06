import matplotlib.pyplot as plt
import numpy as np

n = np.arange(1, 100)

log_n = 3*np.log10(n**2)+2

n_cubico = 8*np.log10(n)

plt.plot(n, log_n, label='g(n)', linestyle='-', marker='o')
plt.plot(n, n_cubico, label='h(n)', linestyle='--', marker='x')

plt.xlabel('n')
plt.ylabel('Valor')
plt.title('Comparação entre g(n) e h(n)')

plt.legend()
plt.savefig("parte1.jpg", dpi=600)