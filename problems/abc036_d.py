n = int(input())
node = [[] for _ in range(n)]  # 隣接リスト
e = []
for i in range(n - 1):
    x, y = map(int, input().split())
    e.append((x - 1, y - 1))
    node[x - 1].append(y - 1)
    node[y - 1].append(x - 1)

from collections import deque

mod = 10 ** 9 + 7
p = [-1] * n  # p[i] はi の親。根なら-1
q = deque([0])  # 根はどこでも良い
r = []  # トポロジカルソート.根から浅い順番にソートされて入っている


# dfs ：　トポロジカルソートと葉ノードのdp初期化
while q:
    i = deque.popleft(q)
    r.append(i)
    # print(node[i])
    for a in node[i]:  # i の子node を探索する5

        if p[a] != -1:
            continue
        p[a] = i
        node[a].remove(i)  # 子への頂点のみを持つ
        deque.append(q, a)


dp_black = [1] * n
dp_white = [1] * n

for i in r[::-1]:  # 葉ノードから順番にdpを埋める
    for j in node[i]:  # 子ノードからの値を足していく
        dp_black[i] *= dp_white[j]
        dp_white[i] *= dp_white[j] + dp_black[j]
        dp_white[i] %= mod
        dp_black[i] %= mod

print((dp_white[0] + dp_black[0]) % mod)
