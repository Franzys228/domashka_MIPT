import sys

lines = [line.strip() for line in sys.stdin if line.strip() != '']
if not lines:
    exit()
n = int(lines[0])
strings = lines[1:1+n]

out = []
for s in strings:
    L = len(s)
    best = L
    for k in range(1, L+1):
        if L % k == 0 and s == s[:k] * (L // k):
            best = k
            break
    out.append(str(best))
print('\n\n'.join(out))
