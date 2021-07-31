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


H, W = [int(_) for _ in input().split()]
N = H * W
check = set()
uf = UnionFind(N)
Q = int(input())
for _ in range(Q):
    q = [int(_) for _ in input().split()]
    if q[0] == 1:
        x = q[1] - 1
        y = q[2] - 1
        i = x + y * H
        check.add(i)
        for j in [x + 1 + y * H, x - 1 + y * H, x + (y + 1) * H, x + (y - 1) * H]:
            if 0 <= j <= H * W - 1 and j in check:
                uf.union(i, j)
    else:
        xa = q[1] - 1
        ya = q[2] - 1
        xb = q[3] - 1
        yb = q[4] - 1
        a = xa + ya * H
        b = xb + yb * H
        if a in check and b in check and uf.same(a, b):
            print("Yes")
        else:
            print("No")
