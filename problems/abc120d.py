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


N, M = [int(_) for _ in input().split()]

# 添字を変換
dic = {}
inv_dic = {}
for i in range(N):
    dic[i + 1] = i
    inv_dic[i] = i + 1

# 各橋がない状態でUFをつくる
bridge = []
for i in range(M):
    bridge.append([int(_) for _ in input().split()])

ans = [N * (N - 1) // 2]
uf = UnionFind(N)

# 逆から考える
for i in range(M - 1, 0, -1):
    A, B = bridge[i]
    # AとBが別にいたときはそれぞれのグループの積を減らす
    if not uf.same(dic[A], dic[B]):
        ans.append(ans[(M - 1) - i] - uf.size(dic[A]) * uf.size(dic[B]))
    else:
        ans.append(ans[(M - 1) - i])
    uf.union(dic[A], dic[B])
for a in ans[::-1]:
    print(a)