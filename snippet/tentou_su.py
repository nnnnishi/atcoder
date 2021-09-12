# 転倒数（バブルソート）

# https://atcoder.jp/contests/agc034/tasks/agc034_b
# https://atcoder.jp/contests/chokudai_S001/tasks/chokudai_S001_j
# https://hcpc-hokudai.github.io/archive/structure_binary_indexed_tree_001.pdf


class BinaryIndexedTree:

    __all__ = ["add", "sumrange", "lower_left"]

    def __init__(self, maxsize=10 ** 6):
        assert maxsize > 0

        self._n = maxsize + 1
        self._bitdata = [0] * (maxsize + 1)

    def add(self, i, x):
        """Add x to A[i] (A[i] += x) """
        assert 0 <= i < self._n

        pos = i + 1
        while pos < self._n:
            self._bitdata[pos] += x
            pos += pos & (-pos)

    # iまでの和
    def running_total(self, i):
        """ Return sum of (A[0] ... A[i]) """
        assert -1 <= i < self._n

        if i == -1:
            return 0
        returnval = 0
        pos = i + 1
        while pos:
            returnval += self._bitdata[pos]
            pos -= pos & (-pos)
        return returnval

    def sumrange(self, lo=0, hi=None):
        """ Return sum of (A[lo] ... A[hi]) """
        if lo < 0:
            raise ValueError("lo must be non-negative")
        if hi is None:
            hi = self._n

        return self.running_total(hi) - self.running_total(lo - 1)

    # 変数を0-1にしておくと指定された要素が何番目に小さいかがわかる
    def lower_left(self, total):
        """Return min-index satisfying {sum(A0 ~ Ai) >= total}
        only if Ai >= 0 (for all i)
        """
        if total < 0:
            return -1
        pos = 0
        k = 1 << (self._n.bit_length() - 1)
        while k > 0:
            if pos + k < self._n and self._bitdata[pos + k] < total:
                total -= self._bitdata[pos + k]
                pos += k
            k //= 2
        return pos


N = int(input())
a = [int(_) for _ in input().split()]

# 要素の最大値+1を()内に入れておけば十分,空で生成すると10**6の初期化リストができる
bit = BinaryIndexedTree()
ans = 0
for i, a in enumerate(a):
    ans += i - bit.running_total(a)
    bit.add(a, 1)
print(ans)
