import sys

input = sys.stdin.readline
N = int(input())
C1 = [0] * (N + 1)
C2 = [0] * (N + 1)
for i in range(N):
    c, p = [int(_) for _ in input().split()]
    if c == 1:
        C1[i + 1] = p
    else:
        C2[i + 1] = p

for i in range(1, N + 1):
    C1[i] = C1[i] + C1[i - 1]
    C2[i] = C2[i] + C2[i - 1]

Q = int(input())
for _ in range(Q):
    l, r = [int(_) for _ in input().split()]
    print(C1[r] - C1[l - 1], C2[r] - C2[l - 1])

