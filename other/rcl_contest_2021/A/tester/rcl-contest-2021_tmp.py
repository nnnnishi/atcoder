"""
# メモ
1つを0に：log2(10**8) = 26.57 -> 1桁増えると約3増える 
-> Mに限りがあるので小さいAは諦める -> 26回くらい自身でたせば10**8にできる 
全部0に：log2(10**8)*300 = 7972.62
ボーナス点：1000 - K
Aは一様ランダム

# 方針
1. 入力
2. 自身の足し合わせでKになれる数：divに含まれるかチェック　
3. 適当な局所探索でなるべく小さくする（制限時間内）
4. 出力
"""
from itertools import product
from random import random, randrange, sample, shuffle, choice, uniform
from time import time
from sys import stdin

input = stdin.readline
debug = True
time_limit = 1.8
case = 0
if not debug:
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
else:
    with open(f"input_{case}.txt") as reader:
        N, M, K = map(int, reader.readline().split())
        A = list(map(int, reader.readline().split()))


# 事前に自身で足し合わせてKになるもの：div
div = []
c = K
# 何回でKになれるかのdict
beK = {}
n = 1
while c > 1:
    if c % 2 == 0:
        c //= 2
        div.append(c)
        beK[c] = n
        n += 1
    else:
        break

divs = set(div)


def main():
    start = time()
    # 2. 自身の足し合わせでKになれる数：divに含まれるかチェック
    ac = [False] * N
    # Kにできるかず
    query = []
    cnt = 0
    for i in range(N):
        if A[i] in divs:
            ac[i] = True
            for _ in range(beK[A[i]]):
                query.append((i, i))
            cnt += beK[A[i]]

    # 3. 適当な局所探索で更新
    while time() - start < time_limit and cnt < M:
        for i in range(N):
            best_j = -1
            best_diff = 0
            if not ac[i] and cnt < M:
                for j in range(N):
                    if A[i] - (A[i] + A[j]) % K > best_diff:
                        best_j = j
                        best_diff = A[i] - ((A[i] + A[j]) % K)
            if best_j != -1:
                query.append((i, best_j))
                A[i] = (A[i] + A[j]) % K
                cnt += 1
    # 4. 出力
    if debug:
        with open(f"output_{case}.txt", "w") as writer:
            for i, j in query:
                writer.write(f"{i} {j}\n")

    else:
        # 本番
        for i, j in query:
            print(i, j)
    return


main()