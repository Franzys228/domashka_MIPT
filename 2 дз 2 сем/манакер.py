import sys

s = sys.stdin.read().strip()
n = len(s)

d1 = [0] * n
l, r = 0, -1
for i in range(n):
    k = 1 if i > r else min(d1[l + r - i], r - i + 1)
    while i - k >= 0 and i + k < n and s[i - k] == s[i + k]:
        k += 1
    d1[i] = k
    if i + k - 1 > r:
        l = i - k + 1
        r = i + k - 1

d2 = [0] * n
l, r = 0, -1
for i in range(n):
    k = 0 if i > r else min(d2[l + r - i + 1], r - i + 1)
    while i - k - 1 >= 0 and i + k < n and s[i - k - 1] == s[i + k]:
        k += 1
    d2[i] = k
    if i + k - 1 > r:
        l = i - k
        r = i + k - 1

total = sum(d1) + sum(d2)
print(total)
