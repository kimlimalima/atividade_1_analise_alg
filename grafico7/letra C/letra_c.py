import matplotlib.pyplot as plt
import numpy as np

n = np.arange(1, 100)

hn = n**(1/2)
omega_log_n= np.log10(n)

plt.plot(n, hn, label='h(n)', linestyle='-', marker='o')
plt.plot(n, omega_log_n, label='Omega(log n)', linestyle='--', marker='x')

plt.xlabel('n')
plt.ylabel('Valor')
plt.title('Comparação entre h(n) e Omega(log n)')

plt.legend()
plt.savefig("parteC.jpg", dpi=600)