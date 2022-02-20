# 転倒数（バブルソート）
# 自分より左にあるかずで大きいものを数えて足せばいい
# 小さいものから順に、左からある大きいものの数だけswapしていけばソートされる
# https://ikatakos.com/pot/programming_algorithm/dynamic_programming/inversion
# https://atcoder.jp/contests/agc034/tasks/agc034_b
# https://atcoder.jp/contests/chokudai_S001/tasks/chokudai_S001_j
# https://hcpc-hokudai.github.io/archive/structure_binary_indexed_tree_001.pdf
# https://juppy.hatenablog.com/entry/2018/11/17/%E8%9F%BB%E6%9C%AC_python_Binary_Indexed_Tree_%E7%AB%B6%E6%8A%80%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0


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

# 0の配列で初期化、iにaiをいれて、左に自分より小さい数の和をチェックできるようにする
bit = BinaryIndexedTree(N + 1)
ans = 0
for i, a in enumerate(a):
    # aより左のもの（小さいもの）の数: running_total(a)
    # aよりも大きいものの数: i - running_total(a)
    ans += i - bit.running_total(a)
    # aにの部分にチェックをいれる
    bit.add(a, 1)
print(ans)
