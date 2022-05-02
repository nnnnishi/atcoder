from collections import defaultdict
import math

N, M = [int(_) for _ in input().split()]
G = [[] for _ in range(N)]
G_l = [[] for _ in range(N)]
e = []
n2cnt = defaultdict(int)
for _ in range(M):
    a, b = [int(_) for _ in input().split()]
    e.append([a - 1, b - 1])
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)
    n2cnt[a - 1] += 1
    n2cnt[b - 1] += 1

# 大きなノードに向かうグラフを作る
for a, b in e:
    if n2cnt[a] > math.sqrt(2 * M):
        G_l[b].append(a)
    if n2cnt[b] > math.sqrt(2 * M):
        G_l[a].append(b)
# 隣接数が少ないノードはmaxの色をみる
# 隣接数が多いノードは逐次更新する
c1 = [1] * N
c2 = [1] * N
t = [0] * N

Q = int(input())
for q in range(1, Q + 1):
    x, y = [int(_) for _ in input().split()]
    x -= 1
    # いろを出力
    if n2cnt[x] > math.sqrt(2 * M):
        print(c2[x])
        # print("here")
    else:
        # 最後に更新されたノード
        tmax = max([t[nx] for nx in G[x]] + [t[x]])
        for nx in G[x] + [x]:
            if t[nx] == tmax:
                print(c1[nx])
                break
    # print(c1)
    # print(c2)
    # print(t)
    # 塗り替える
    # それ自身
    c1[x] = y
    c2[x] = y
    t[x] = q
    # 大きいやつ
    for i in G_l[x]:
        c2[i] = y
