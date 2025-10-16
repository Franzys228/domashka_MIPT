import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('iris_data.csv')
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

species_counts = df['Species'].value_counts()
ax1.pie(species_counts.values, labels=species_counts.index, autopct='%1.1f%%')
ax1.set_title('Виды ирисов')

petal_length = df['PetalLengthCm']
cats = ['≤1.2', '1.2-1.5', '>1.5']
counts = [
    len(petal_length[petal_length <= 1.2]),
    len(petal_length[(petal_length > 1.2) & (petal_length <= 1.5)]),
    len(petal_length[petal_length > 1.5])
]
ax2.pie(counts, labels=cats, autopct='%1.1f%%')
ax2.set_title('Длина лепестка')
plt.show()
