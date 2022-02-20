# unionfind
# unionfind
from collections import defaultdict


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        """
        経路圧縮
        """
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        """
        union by size込み、sizeからrankにしたりなくしたりしてもよい
        """
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        # Sizeの大きい方につける
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


import sys

input = sys.stdin.readline

N, Q = [int(_) for _ in input().split()]
G = [[] for _ in range(N)]
uf = UnionFind(N)
for i in range(Q):
    a, b = [int(_) for _ in input().split()]
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)
# print(G)
ans = [0]
cnt = 0
bf = 0
for i in range(N - 1, 0, -1):
    cnt = 1
    G[i].sort(reverse=True)
    for x in G[i]:
        if x > i:
            if not uf.same(i, x):
                uf.union(i, x)
                cnt -= 1
        else:
            break
    ans.append(bf + cnt)
    bf += cnt
# print(ans)
print(*ans[::-1], sep="\n")
