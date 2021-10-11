N, A, B = [int(_) for _ in input().split()]
sums = 0
maxs = 0
mins = 10 ** 9
for i in range(N):
    s = int(input())
    sums += s
    mins = min(mins, s)
    maxs = max(maxs, s)

if maxs - mins == 0:
    exit(print(-1))
else:
    P = B / (maxs - mins)

Q = A - (P * sums / N)

print(P, Q)

