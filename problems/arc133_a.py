import sys

input = sys.stdin.readline

N = int(input())
A = [int(_) for _ in input().split()]

d = 0
for i in range(N - 1):
    if A[i] > A[i + 1]:
        d = A[i]
        break
    else:
        continue
if d == 0:
    d = A[N - 1]
ans = []
for a in A:
    if a != d:
        ans.append(a)
print(*ans)
