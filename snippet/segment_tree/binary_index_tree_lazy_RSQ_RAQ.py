# RSQ and RAQ (Lazy Binary Index Tree)
# https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/2/DSL_2_G
# https://onlinejudge.u-aizu.ac.jp/solutions/problem/DSL_2_G/review/4692229/hiro0229/Python3
# https://juppy.hatenablog.com/entry/2018/11/17/%E8%9F%BB%E6%9C%AC_python_Binary_Indexed_Tree_%E7%AB%B6%E6%8A%80%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0


class LazyBinaryIndexTree:
    """ 区間加算BIT(区間加算・区間合計取得) """

    def __init__(self, N):
        self.N = N + 1
        self.tree = [0] * (N + 1)
        self.lazy = [0] * (N + 1)

    def _add(self, data, k, x):
        while k < self.N:  # k <= Nと同義
            data[k] += x
            k += k & -k

    def _sum(self, data, k):
        s = 0
        while k:
            s += data[k]
            k -= k & -k
        return s

    def add(self, l, r, x):
        """ 区間[l,r)に値xを追加 """

        self._add(self.tree, l, -x * (l - 1))
        self._add(self.tree, r, x * (r - 1))
        self._add(self.lazy, l, x)
        self._add(self.lazy, r, -x)

    def sum(self, l, r):
        """ 区間[l,r)の和を取得 """
        return (
            self._sum(self.lazy, r - 1) * (r - 1)
            + self._sum(self.tree, r - 1)
            - self._sum(self.lazy, l - 1) * (l - 1)
            - self._sum(self.tree, l - 1)
        )


N, Q = [int(_) for _ in input().split()]
# 要素の最大値を()内に入れておけば十分
bit = LazyBinaryIndexTree(N)
ans = []
for _ in range(Q):
    q, *com = [int(_) for _ in input().split()]
    if q == 0:
        s, t, x = com
        bit.add(s, t + 1, x)
    else:
        s, t = com
        ans.append(bit.sum(s, t + 1))
print(*ans, sep="\n")
