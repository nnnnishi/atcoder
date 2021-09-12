# Kruskal O(Elog(V))
# 枝コストの小さい順にノードをつなげる

from collections import defaultdict


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


# Kruskal法により最小全域木を求める
def kruskal(N, es, tot):
    res = N - 1
    uf = UnionFind(N)
    c = 0
    for e in es:
        c = e[0]
        if c > 0 and res == 0:
            break
        if not uf.same(e[1] - 1, e[2] - 1):
            uf.union(e[1] - 1, e[2] - 1)
            tot -= c
            res -= 1
        else:
            if c < 0:
                tot += -c
    return tot


N, M = list(map(int, input().split()))
tot = 0
cost = {}
e = []
for i in range(M):
    v1, v2, c = [int(_) for _ in input().split()]
    # 自己ループで報酬ありは加える
    if v1 == v2 and c > 0:
        tot += c
        continue
    # 自己ループでない
    e.append([c, v1, v2])
    tot += c
e.sort()

ans = kruskal(N, e, tot)

print(ans)