import sys
from operator import itemgetter

input = sys.stdin.readline
N = int(input())
L = []
for _ in range(N):
    L.append([int(_) for _ in input().split()])
L.sort(key=itemgetter(1))
ans = 0
ps = 0
pe = 0
for s, e in L:
    if pe <= s:
        ans += 1
        pe = e

print(ans)
