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

ans = 0
a = [[int(_) for _ in input().split()] for _ in range(4)]
print(a)

def dfs(i,):
    global ans
    if i == 15:
        if check()
for
N = 16
uf = UnionFind(16)
# 添字を変換
dic = {}
inv_dic = {}
for i in range(N):
    dic[i + 1] = i
    inv_dic[i] = i + 1

bridge = []
for i in range(M):
    bridge.append([int(_) for _ in input().split()])

for i in range(M):
    A, B = bridge[i]
    uf.union(dic[A], dic[B])
