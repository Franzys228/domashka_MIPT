n = int(input())
lst = list(map(int, input().split()))

for i in range(n):
    less = 0
    more = 0
    for j in range(n):
        if lst[j] < lst[i]:
            less += 1
        elif lst[j] > lst[i]:
            more += 1
    if less == more:
        print(lst[i])
        break
