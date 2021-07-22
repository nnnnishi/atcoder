# unionfind
from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations
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


N, K, L = [int(_) for _ in input().split()]
uf_a = UnionFind(N)
uf_b = UnionFind(N)

# どうろ
for i in range(K):
    p, q = [int(_) for _ in input().split()]
    uf_a.union(p - 1, q - 1)

# てつどう
for i in range(L):
    p, q = [int(_) for _ in input().split()]
    uf_b.union(p - 1, q - 1)

ans = []
L = []
for i in range(N):
    fa = uf_a.find(i)
    fb = uf_b.find(i)
    L.append((fa, fb))
c = Counter(L)
for l in L:
    ans.append(c[l])
print(*ans)