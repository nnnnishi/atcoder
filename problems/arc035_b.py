from collections import defaultdict


N = int(input())
d = defaultdict(int)
for i in range(N):
    t = int(input())
    d[t] += 1
L = []
for k in d.keys():
    L.append(k)
L.sort()
MOD = 10 ** 9 + 7
pat = 1
tim = 0
elapsed = 0
ans = 0
for l in L:
    for p in range(d[l], 0, -1):
        pat *= p
        pat %= MOD
        elapsed += l
        ans += elapsed
print(ans)
print(pat)
