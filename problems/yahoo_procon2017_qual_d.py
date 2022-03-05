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


Q, K = [int(_) for _ in input().split()]
d_set = set()
query = []
for _ in range(Q):
    q = [int(_) for _ in input().split()]
    d_set.add(q[1])
    query.append(q)
lenD = len(d_set)
d_list = list(d_set)
d_list.sort()
i2d = {}
d2i = {}
for i in range(lenD):
    i2d[i] = d_list[i]
    d2i[d_list[i]] = i
print(i2d, d2i)

# 要素の最大値を()内に入れておけば十分
ans = []
print(lenD)
cum_bit = LazyBinaryIndexTree(lenD)
ans_bit = LazyBinaryIndexTree(lenD)
print(cum_bit.tree)
for i in range(lenD):
    cum_bit.add(i + 1, i + 2, i2d[i] * K)
    print(cum_bit.tree, cum_bit.lazy)
print("*" * 10)
for q in query:
    c, *cmd = q
    # dにaだけうる
    if c == 1:
        d, a = cmd
        stock = cum_bit.sum(d2i[d] + 1, d2i[d] + 2)
        if stock >= a:
            cum_bit.add(d2i[d] + 1, lenD, -a)
            ans_bit.add(d2i[d] + 1, d2i[d] + 2, a)
        else:
            cum_bit.add(d2i[d] + 1, lenD + 1, -stock)
            ans_bit.add(d2i[d] + 1, d2i[d] + 2, stock)
        print(cum_bit.tree, cum_bit.lazy)
        print(ans_bit.tree, ans_bit.lazy)
        print(cum_bit.tree, cum_bit.lazy)
        print("*" * 10)
    # チェックする
    else:
        d = cmd[0]
        ans.append(ans_bit.sum(1, d2i[d] + 2))
        print("check")
        print(cum_bit.tree, cum_bit.lazy)
        print(ans_bit.tree, ans_bit.lazy)
        print(cum_bit.tree, cum_bit.lazy)
        print("*" * 10)

print(*ans, sep="\n")
