N = int(input())
B = [int(_) for _ in input().split()]
ans = B[0] + B[N - 2]
for i in range(N - 2):
    ans += min(B[i], B[i + 1])

print(ans)
