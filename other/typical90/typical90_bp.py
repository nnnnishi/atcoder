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


N = int(input())
Q = int(input())


d = {}
query = []
# クエリ先読み
for i in range(Q):
    t, x, y, v = [int(_) for _ in input().split()]
    query.append([t, x, y, v])
    if t == 0:
        d[(x - 1, y - 1)] = v

base = [-1] * N
i = 0
while i < N - 1:
    # i が頭
    if (i, i + 1) in d:
        base[i] = 0
        base[i + 1] = d[(i, i + 1)] - base[i]
        i += 1
        # i　が前からつづく
        while i < N - 1:
            if (i, i + 1) in d:
                base[i + 1] = d[(i, i + 1)] - base[i]
                i += 1
            else:
                i += 1
                break
    else:
        i += 1

uf = UnionFind(N)
for t, x, y, v in query:
    if t == 0:
        uf.union(x - 1, y - 1)
    else:
        if uf.same(x - 1, y - 1):
            diff = v - base[x - 1]
            if abs((x - 1) - (y - 1)) % 2 == 1:
                print(base[y - 1] - diff)
            else:
                print(base[y - 1] + diff)
        else:
            print("Ambiguous")
