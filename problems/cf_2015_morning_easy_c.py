N, K, M, R = [int(_) for _ in input().split()]
s = []
for i in range(N - 1):
    s.append(int(input()))
s.sort(reverse=True)

if sum(s[:K]) >= (K * R):
    print(0)
elif sum(s[: K - 1]) + M < (K * R):
    print(-1)
else:
    print((K * R) - sum(s[: K - 1]))

