from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

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
x_list = []
y_list = []
G = []
for i in range(N):
    x, y = [int(_) for _ in input().split()]
    x_list.append((x, i))
    y_list.append((y, i))
x_list.sort()
y_list.sort()
q = []
for i in range(N - 1):
    d = x_list[i + 1][0] - x_list[i][0]
    i1 = x_list[i][1]
    i2 = x_list[i + 1][1]
    heappush(q, (d, i1, i2))
for i in range(N - 1):
    d = y_list[i + 1][0] - y_list[i][0]
    i1 = y_list[i][1]
    i2 = y_list[i + 1][1]
    heappush(q, (d, i1, i2))

cost = 0
uf = UnionFind(N)
while len(q) > 0:
    d, i1, i2 = heappop(q)
    if not uf.same(i1, i2):
        cost += d
        uf.union(i1, i2)
print(cost)