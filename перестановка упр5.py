lst = list(input())
lst = [lst[-1]] + lst[:-1]
print(''.join(lst))
