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


def main():
    start = time()
    cnt = 0
    query = []
    # 3. 適当な局所探索で更新
    while time() - start < time_limit and cnt < M:
        best_j = -1
        min_score = 0
        for i in range(N):
            for j in range(N):
                for n in range(1, 4):
                    if (A[i] + n * A[j]) % K < min_score:
                        best_j = j
                        best_n = n
                        min_score = (A[i] + A[j]) % K
            if best_j != -1:
                for _ in range(best_n):
                    query.append((i, best_j))
                    cnt += 1
                A[i] = (A[i] + best_n * A[best_j]) % K

    # print(len(query))
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