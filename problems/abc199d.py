# unionfind
from collections import defaultdict

N, M = list(map(int, input().split()))
graph = []
e = []
for i in range(N):
    graph.append([])
for i in range(M):
    Ai, Bi = list(map(int, input().split()))
    e.append([Ai - 1, Bi - 1])
    graph[Ai - 1].append(Bi - 1)
    graph[Bi - 1].append(Ai - 1)


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return "\n".join(f"{r}: {m}" for r, m in self.all_group_members().items())


# 深さ優先
def dfs(i):
    global t
    t.append(i)
    visited.add(i)
    # 次行く場所を全探索
    for j in graph[i]:
        if j not in visited:
            dfs(j)

    return


def dfs2(i, c, nodes):
    """
    index, 色, iに対応する頂点
    """
    v = nodes[i]
    colors[v] = c
    # つぎの頂点
    for next_v in graph[v]:
        # 隣接の頂点がすでに塗られていて同一だったらアウト
        if colors[next_v] == colors[v]:
            return 0
    # 最後のノードまでたどり着いていたら1をかえす
    if i == len(nodes) - 1:
        return 1
    res = 0
    rest = {0, 1, 2}
    # 色の順番の早い方から次に進む
    for rest_c in rest:
        res += dfs2(i + 1, rest_c, nodes)
        # でてきたら色を無色にもどす
        colors[nodes[i + 1]] = -1
    return res


uf = UnionFind(N)

for i in range(M):
    A, B = e[i]
    uf.union(A, B)

colors = [-1] * N
# ufのグループごとにチェック
ans = 1
for r in uf.roots():
    visited = set()
    t = []
    # tourを生成
    dfs(r)
    # print(t)
    cnt = dfs2(0, 0, t)
    ans *= 3 * cnt

print(ans)