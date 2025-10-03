lst = list(input())
for i in range(0, len(lst) - 1, 2):
    lst[i], lst[i + 1] = lst[i + 1], lst[i]
print(''.join(lst))
