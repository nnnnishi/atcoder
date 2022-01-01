N = int(input())
ans = [0] * (N + 1)
ans[0] = 1
for i in range(1, N + 1):
    if i == 1:
        ans[i] = ans[i - 1]
    else:
        ans[i] = ans[i - 1] + ans[i - 2]
print(ans[N])
