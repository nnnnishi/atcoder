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


Y, X = [int(_) for _ in input().split()]
uf = UnionFind(Y * X)
C = [[0] * X for _ in range(Y)]
Q = int(input())
for _ in range(Q):
    A = [int(_) for _ in input().split()]
    if A[0] == 1:
        y, x = A[1], A[2]
        y -= 1
        x -= 1
        idx = y * X + x
        C[y][x] = 1
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if 0 <= y + dy < Y and 0 <= x + dx < X:
                if C[y + dy][x + dx] == 1:
                    uf.union(idx, (y + dy) * X + (x + dx))
    else:
        y1, x1, y2, x2 = A[1], A[2], A[3], A[4]
        y1 -= 1
        x1 -= 1
        y2 -= 1
        x2 -= 1
        if y1 * X + x1 == y2 * X + x2:
            if C[y1][x1] == 0:
                print("No")
            else:
                print("Yes")
        else:
            if uf.same(y1 * X + x1, y2 * X + x2):
                print("Yes")
            else:
                print("No")

