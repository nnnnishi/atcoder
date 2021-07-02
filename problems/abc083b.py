N, A, B = list(map(int, input().split()))

ans = 0
for n in range(1, N + 1):
    tmp = sum(map(int, list(str(n))))
    if A <= tmp <= B:
        ans += n

print(ans)
