import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(2, 2)
for i, n in enumerate([50, 200, 1000, 5000]):
    data = np.random.normal(0, 1, n)
    ax = axes[i//2, i%2]
    ax.hist(data, bins=15, density=True, alpha=0.6)
    x = np.linspace(-4, 4, 100)
    ax.plot(x, (1/np.sqrt(2*np.pi))*np.exp(-x**2/2), 'r-')
    ax.set_title(f'n = {n}')
plt.tight_layout()
plt.show()
