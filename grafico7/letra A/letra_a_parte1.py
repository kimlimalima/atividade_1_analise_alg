import matplotlib.pyplot as plt
import numpy as np

n = np.arange(1, 100)


fn = 3*n**3 + 20*n**2 + 5

gn = 3 * np.log10

hn = n**2


plt.plot(n, fn, label='f(n)', linestyle='-', marker='o')
plt.plot(n, gn, label='g(n)', linestyle='--', marker='x')
plt.plot(n, hn, label='h(n)', linestyle='--', marker='x')

plt.xlabel('n')
plt.ylabel('Valor')
plt.title('Comparação entre 3*log10(n**2)+2 e log10(n)')

plt.legend()
plt.savefig("parte1.jpg", dpi=600)