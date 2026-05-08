import sys

s = sys.stdin.readline().strip()
n = len(s)
t = s + s

sa = list(range(2 * n))
k = 1
rank = [ord(c) for c in t]
tmp = [0] * (2 * n)

while True:
    sa.sort(key=lambda x: (rank[x], rank[x + k] if x + k < 2 * n else -1))
    tmp[sa[0]] = 0
    for i in range(1, 2 * n):
        prev, cur = sa[i-1], sa[i]
        prev_key = (rank[prev], rank[prev + k] if prev + k < 2 * n else -1)
        cur_key = (rank[cur], rank[cur + k] if cur + k < 2 * n else -1)
        tmp[cur] = tmp[prev] + (prev_key < cur_key)
    rank, tmp = tmp, rank
    if rank[sa[-1]] == 2 * n - 1:
        break
    k <<= 1

order = [i for i in sa if i < n]
pos = order.index(0) + 1
last_col = ''.join(s[(i - 1) % n] for i in order)

print(pos)
print(last_col)
