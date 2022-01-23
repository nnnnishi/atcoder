import sys

input = sys.stdin.readline

N, Q = list(map(int, input().split()))
A = [int(_) for _ in input().split()]
d = {}
for i, a in enumerate(A):
    d.setdefault(a, [])
    d[a].append(i + 1)

for _ in range(Q):
    x, k = [int(_) for _ in input().split()]
    if x not in d:
        print(-1)
    else:
        if len(d[x]) < k:
            print(-1)
        else:
            print(d[x][k - 1])
