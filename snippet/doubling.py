# ダブリング
# 一つの局面に複数の要素があり、互いに遷移するとき、同じ操作を繰り返したN回目の状態を求めるのに利用できる
# 素朴にN回後の移動先を計算するとO(N)だが、2乗ずつの移動先を作っておくことでO(logN)まで減らせる
# 要素数をX、移動回数をNとして、前処理がO(XlogN)、遷移先の計算がO(X)
# https://blog.hamayanhamayan.com/entry/2019/08/07/204315

S = list(input())
dp = [[0] * len(S) for _ in range(2 ** 6 + 1)]

for i in range(len(S)):
    if S[i] == "R":
        dp[0][i] = i + 1
    else:
        dp[0][i] = i - 1

for p in range(2 ** 6):
    for i in range(len(S)):
        dp[p + 1][i] = dp[p][dp[p][i]]

ans = [0] * len(S)

for i in range(len(S)):
    ans[dp[2 ** 6][i]] += 1

print(*ans)
