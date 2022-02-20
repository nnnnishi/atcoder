# unionfind
from collections import defaultdict
import sys
from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

input = sys.stdin.readline


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


N, M = [int(_) for _ in input().split()]
uf = UnionFind(N)
res = [int(_) for _ in input().split()]
ans = []

for _ in range(M):
    A, B = [int(_) for _ in input().split()]
    A -= 1
    B -= 1
    res[A] -= 1
    res[B] -= 1

    if uf.same(A, B) or res[A] < 0 or res[B] < 0:
        print(-1)
        exit()
    uf.union(A, B)
res_l = defaultdict(lambda: [])
res_c = defaultdict(lambda: 0)
for i, r in enumerate(res):
    if r > 0:
        pi = uf.find(i)
        res_c[pi] += r
        res_l[pi] += r * [i]

if sum(res_c.values()) != 2 * (len(res_c) - 1):
    print(-1)
    exit()

one_q = []
two_q = []
for k, v in res_c.items():
    if v > 1:
        two_q.append(k)
    elif v == 1:
        one_q.append(k)

"""
print(res_l)
print(res_c)
print(one_q)
print(two_q)
"""

while len(one_q) > 0:
    if len(two_q) > 0:
        pA = one_q.pop()
        pB = two_q.pop()
        # print(pA, pB)
        res_c[pA] -= 1
        res_c[pB] -= 1
        cA = res_l[pA].pop()
        cB = res_l[pB].pop()
        ans.append([cA + 1, cB + 1])
        if res_c[pB] == 1:
            one_q.append(pB)
        else:
            two_q.append(pB)

    elif len(one_q) == 2:
        # print(one_q), print(res_l)
        pA = one_q.pop()
        cA = res_l[pA].pop()
        pB = one_q.pop()
        cB = res_l[pB].pop()
        ans.append([cA + 1, cB + 1])
    else:
        print(-1)
        exit()

if len(two_q) == 0:
    for i, j in ans:
        print(i, j)
else:
    print(-1)

