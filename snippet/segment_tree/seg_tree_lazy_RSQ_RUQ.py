"""Range Sum Query & Range Uodate Query"""
# https://onlinejudge.u-aizu.ac.jp/solutions/problem/DSL_2_I/review/5306669/genomas/Python3
import sys

input = sys.stdin.readline


from operator import add  # 単位元は0

# 1-indexed
class LazySegTree_u:  # 抽象化"区間更新"区間取得遅延セグ木
    def __init__(self, vector, _operator=min, identity=float("inf")):  # O(N)
        self._operator = _operator  # Min,Max,Sum,Xorなどの二項演算子
        self.len_vector = len(vector)  # 元の配列の長さ
        self.num_leaf = (
            1 << (len(vector) - 1).bit_length()
        )  # num_leafはlen_vector以上の整数で最小の2冪
        self.identity = identity  # 演算self._operatorの単位元
        self.node = [identity] * (2 * self.num_leaf)  # self.nodeを演算の単位元で初期化
        self.lazy = [None] * (2 * self.num_leaf)

        # 配列の値を葉にセット
        for i in range(self.len_vector):
            self.node[self.num_leaf + i] = vector[i]
        # 構築
        for i in range(self.num_leaf - 1, 0, -1):
            self.node[i] = self._operator(self.node[2 * i], self.node[2 * i + 1])

    def _gindex(self, l, r):  # 伝搬対象区間をgenerate
        L = (l + self.num_leaf) >> 1
        R = (r + self.num_leaf) >> 1
        lc = 0 if l & 1 else (L & -L).bit_length()
        rc = 0 if r & 1 else (R & -R).bit_length()
        for i in range((self.num_leaf - 1).bit_length()):
            if rc <= i:
                yield R
            if L < R and lc <= i:
                yield L
            L >>= 1
            R >>= 1

    def _propagate(self, *ids):  # 遅延伝搬
        for i in reversed(ids):
            val = self.lazy[i - 1]
            if val is None:
                continue
            V = val >> 1
            self.lazy[2 * i - 1] = V
            self.lazy[2 * i] = V
            self.node[2 * i - 1] = V
            self.node[2 * i] = V
            self.lazy[i - 1] = None

    def update(self, l, r, x):  # 区間[l,r)更新 # O(logN)
        (*ids,) = self._gindex(l, r)
        self._propagate(*ids)

        L = l + self.num_leaf
        R = r + self.num_leaf
        while L < R:
            if R & 1:
                R -= 1
                self.lazy[R - 1] = x
                self.node[R - 1] = x
            if L & 1:
                self.lazy[L - 1] = x
                self.node[L - 1] = x
                L += 1
            L >>= 1
            R >>= 1
            x <<= 1
        for i in ids:
            self.node[i - 1] = self._operator(self.node[2 * i - 1], self.node[2 * i])

    def query(self, l, r):  # 区間[l,r)取得 # O(logN)
        (*ids,) = self._gindex(l, r)
        self._propagate(*ids)

        L = l + self.num_leaf
        R = r + self.num_leaf
        res = self.identity
        while L < R:
            if R & 1:
                R -= 1
                res = self._operator(res, self.node[R - 1])
            if L & 1:
                res = self._operator(res, self.node[L - 1])
                L += 1
            L >>= 1
            R >>= 1
        return res

    def get_point(self, i):  # 一点取得 # O(logN)
        return self.query(i, i + 1)


n, q = map(int, input().split())
initial_list = [0] * n
lst = LazySegTree_u(initial_list, add, 0)

ans = []
for _ in range(q):
    t, *cmd = list(map(int, input().split()))
    if t:
        s, t = cmd
        ans.append(str(lst.query(s, t + 1)))
    else:
        s, t, x = cmd
        lst.update(s, t + 1, x)
print("\n".join(ans))
