arr = list(map(int, input().split()))
x = int(input())
print(arr.index(x) if x in arr else -1)
