import matplotlib.pyplot as plt
import numpy as np

n = np.arange(1, 100)

hn = n**(1/2)

omega = np.log10(n)

plt.plot(n, hn, label='n**(1/2)', linestyle='-', marker='o')
plt.plot(n, omega, label='log10(n)', linestyle='--', marker='x')

plt.xlabel('n')
plt.ylabel('Valor')
plt.title('Comparação entre n**(1/2) e log10(n)')

plt.legend()
plt.savefig("parte1.jpg", dpi=600)