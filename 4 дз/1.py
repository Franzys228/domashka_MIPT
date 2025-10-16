import matplotlib.pyplot as plt
import pandas as pd

data = pd.DataFrame({'X': [1, 2, 3, 4, 5], 'Y': [2.1, 3.8, 6.2, 8.1, 9.9]})
plt.plot(data['X'], data['Y'], 'o-')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()
plt.show()
