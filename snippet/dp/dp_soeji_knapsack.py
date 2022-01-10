# 添字が増えるタイプのDP
# サイコロDP
from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N, D = [int(_) for _ in input().split()]

# 素因数分解、試し割り法
# https://qiita.com/drken/items/a14e9af0ca2d857dad23
# O(root(N))
def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    # root(N)まで試し割り
    while f * f <= n:
        # 割り切れたらその数で割る
        if n % f == 0:
            a.append(f)
            n //= f
        # 割り切れなかったら偶数はとばして次に行く
        else:
            f += 2
    # のこったものが1でなければそれも約数
    if n != 1:
        a.append(n)
    return a


l = prime_factorize(D)

c = Counter(l)

if len(c) > 3:
    exit(print(0))
for k in c.keys():
    if k not in [2, 3, 5]:
        exit(print(0))
a2, a3, a5 = c[2], c[3], c[5]
# dp[2のでたかず][3のでたかず][5のでたかず] = 確率
dp = [
    [[[0] * (a5 + 1) for _ in range(a3 + 1)] for _ in range(a2 + 1)]
    for _ in range(N + 1)
]
# 初回は何も降ってないのですべて0

dp[0][0][0][0] = 1

for i in range(N):
    for a in range(a2 + 1):
        for b in range(a3 + 1):
            for c in range(a5 + 1):
                dp[i + 1][a][b][c] += dp[i][a][b][c] * 1 / 6
                if a + 1 <= a2:
                    dp[i + 1][a + 1][b][c] += dp[i][a][b][c] * 1 / 6
                else:
                    dp[i + 1][a][b][c] += dp[i][a][b][c] * 1 / 6
                if b + 1 <= a3:
                    dp[i + 1][a][b + 1][c] += dp[i][a][b][c] * 1 / 6
                else:
                    dp[i + 1][a][b][c] += dp[i][a][b][c] * 1 / 6
                if a + 2 <= a2:
                    dp[i + 1][a + 2][b][c] += dp[i][a][b][c] * 1 / 6
                elif a + 1 <= a2:
                    dp[i + 1][a + 1][b][c] += dp[i][a][b][c] * 1 / 6
                else:
                    dp[i + 1][a][b][c] += dp[i][a][b][c] * 1 / 6
                if c + 1 <= a5:
                    dp[i + 1][a][b][c + 1] += dp[i][a][b][c] * 1 / 6
                else:
                    dp[i + 1][a][b][c] += dp[i][a][b][c] * 1 / 6
                if a + 1 <= a2 and b + 1 <= a3:
                    dp[i + 1][a + 1][b + 1][c] += dp[i][a][b][c] * 1 / 6
                elif a + 1 <= a2:
                    dp[i + 1][a + 1][b][c] += dp[i][a][b][c] * 1 / 6
                elif b + 1 <= a3:
                    dp[i + 1][a][b + 1][c] += dp[i][a][b][c] * 1 / 6
                else:
                    dp[i + 1][a][b][c] += dp[i][a][b][c] * 1 / 6

print(dp[N][a2][a3][a5])
