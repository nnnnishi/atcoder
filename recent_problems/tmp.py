# unionfind
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


N, K = [int(_) for _ in input().split()]
P = [int(_) for _ in input().split()]
C = [int(_) for _ in input().split()]

uf = UnionFind(N)
# 添字を変換
dic = {}
inv_dic = {}
for i in range(N):
    uf.union(i, P[i] - 1)


def check(r):
    # 1周分のコスト
    N = uf.size(r)
    # print(N)
    if K // N > 0:
        ans = ((K // N) - 1) * sum([C[x] for x in uf.members(r)])
        if ans < 0:
            ans = 0
        res = K - (((K // N) - 1) * N)
    else:
        ans = 0
        res = K
    # 1から循環させる
    cumA = [0] * (3 * N + 1)
    idx = r
    for i in range(3 * N):
        cumA[i + 1] = cumA[i] + C[idx]
        idx = P[idx] - 1
    a = -(10 ** 20)
    # print(uf.members(r))
    # print(ans, res)
    # print(cumA)
    for j in range(1, res + 1):
        for i in range(j, 3 * N + 1):
            a = max(a, cumA[i] - cumA[i - j])
    # print("*", ans + a)
    return ans + a


ans = -(10 ** 20)
for r in uf.roots():
    ans = max(check(r), ans)

print(ans)
