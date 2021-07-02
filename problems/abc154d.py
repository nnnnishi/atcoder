N, K = list(map(int, input().split()))
p = list(map(int, input().split()))

ans = 0
tmp_ans = 0
for i in range(K):
    tmp_ans += p[i] + 1
tmp_ans = tmp_ans / 2
if (N + 1) - K == 1:
    print(tmp_ans)
else:
    for i in range(1, (N + 1) - K):
        tmp_ans = tmp_ans + ((p[K + i - 1] - p[i - 1]) / 2)
        ans = max(tmp_ans, ans)
    print(ans)