# ナップサック復元
# https://qiita.com/drken/items/0c7bab0384438f285f93
# https://github.com/E869120/kyopro_educational_90/blob/main/editorial/056.jpg

from collections import Counter, deque, defaultdict


N, S = [int(_) for _ in input().split()]
query = []
for _ in range(N):
    query.append([int(_) for _ in input().split()])

dp = [[0] * (S + 1) for _ in range(N + 1)]
dp[0][0] = 1
for i in range(N):
    for j in range(S):
        if dp[i][j] == 1:
            if j + query[i][0] <= S:
                dp[i + 1][j + query[i][0]] = 1
            if j + query[i][1] <= S:
                dp[i + 1][j + query[i][1]] = 1

# たどり着いている
if dp[N][S] == 1:
    ans = deque()
    cur_w = S
    for i in range(N, 0, -1):
        # dpテーブルを戻ってそこを通っている
        if cur_w - query[i - 1][0] >= 0 and dp[i - 1][cur_w - query[i - 1][0]] == 1:
            ans.appendleft("A")
            cur_w -= query[i - 1][0]
        else:
            ans.appendleft("B")
            cur_w -= query[i - 1][1]
    print("".join(ans))
else:
    print("Impossible")
