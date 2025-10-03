lst = input().split()
print(max(set(lst), key=lst.count))
