# https://atcoder.jp/contests/tdpc/tasks/tdpc_fibonacci
# https://qiita.com/flour/items/1390b1daedfec545bc94
# O(k^2logN)
class kitamasa:
    def __init__(self, c0, d, mod):
        self.c0 = c0
        self.k = len(c0)
        self.d = d
        self.mod = mod

    def next(self, c):
        next_c = [0] * self.k
        next_c[0] = self.d[0] * c[-1]
        for i in range(1, self.k):
            next_c[i] = c[i - 1] + self.d[i] * c[-1]
            next_c[i] %= self.mod
        next_c[0] %= self.mod
        return next_c

    def double(self, c):
        double_c = [0] * self.k
        cs = [c]
        for i in range(self.k - 1):
            cs += (self.next(cs[-1]),)
        for i, ci in enumerate(cs):
            for j in range(self.k):
                double_c[j] += ci[j] * c[i]
                double_c[j] %= self.mod
        return double_c

    def calc(self, n):
        c = [0] * self.k
        c[1] = 1
        msb = 0
        for i in range(64, -1, -1):
            if n & (1 << i):
                msb = i
                break
        for i in range(msb - 1, -1, -1):
            c = self.double(c)
            if n & (1 << i):
                c = self.next(c)
        return sum(c[i] * self.d[i] for i in range(self.k)) % self.mod


K, N = [int(_) for _ in input().split()]
c = [1] * K
d = [1] * K
k = kitamasa(c, d, 10 ** 9 + 7)
# fib(N)を求める
print(k.calc(N - 1))

