set1 = set([1, 2, 3, 4, 5])
set2 = set([4, 5, 6, 7, 8])

print("Уникальные для set1:", set1 - set2)
print("Уникальные для set2:", set2 - set1)
print("Уникальные для объединения:", set1 ^ set2)
print("Пересечение:", set1 & set2)
