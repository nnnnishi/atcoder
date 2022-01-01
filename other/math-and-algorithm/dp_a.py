N = int(input())
h = [int(_) for _ in input().split()]
ans = [0] * N
for i in range(1, N):
    if i == 1:
        ans[i] = abs(h[i] - h[i - 1])
    else:
        ans[i] = min(
            ans[i - 1] + abs(h[i] - h[i - 1]), ans[i - 2] + abs(h[i] - h[i - 2])
        )
print(ans[N - 1])
