N = int(input())
P = [int(_) for _ in input().split()]
ans = 0
minp = 10 ** 10
for i in range(N):
    minp = min(P[i], minp)
    if minp == P[i]:
        ans += 1
print(ans)