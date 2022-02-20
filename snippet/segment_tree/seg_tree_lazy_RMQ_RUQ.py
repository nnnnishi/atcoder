import sys

input = sys.stdin.readline
# RMQ_RUQ: 最小値などを求める、値を更新する
# (RMQ_RAQ: 最小値などを求める、値を加算する は別コード)
# https://smijake3.hatenablog.com/entry/2018/11/03/100133#%E3%82%B3%E3%83%BC%E3%83%89%E5%AE%9F%E8%A3%85-RMQ-and-RUQ
# https://qiita.com/takayg1/items/c811bd07c21923d7ec69
def segfunc(x, y):
    # min
    if x < y:
        return x
    else:
        return y


ide_ele = 2 ** 31 - 1


class LazySegTree:
    def __init__(self, init_val, segfunc, ide_ele):
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        # 遅延用の配列ももっておくところだけsegtreeと違う
        self.lazy = [None] * 2 * self.num
        # *** segtreeとおなじ ***
        # 配列の値を葉にセット
        for i in range(n):
            # 葉の部分を初期値でうめる
            self.tree[self.num + i] = init_val[i]
        # 葉よりうえの木をうめてく
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def gindex(self, l, r):
        """
        伝播される区間のindexを下から上に全列挙
        """
        l += self.num
        r += self.num
        lm = l >> (l & -l).bit_length()
        rm = r >> (r & -r).bit_length()
        while r > l:
            if l <= lm:
                yield l
            if r <= rm:
                yield r
            r >>= 1
            l >>= 1
        while l:
            yield l
            l >>= 1

    def propagates(self, *ids):
        """
        逆順にして上から下にidxを処理、Range Update Query用の伝播処理
        """
        for i in reversed(ids):
            v = self.lazy[i]
            if v is None:
                continue
            self.lazy[i] = None
            # 子にvをわたす
            self.lazy[2 * i] = v
            self.lazy[2 * i + 1] = v
            self.tree[2 * i] = v
            self.tree[2 * i + 1] = v

    def update(self, l, r, x):
        """
        [l,r)でxを適用する区間更新: Range Update Query
        """
        (*ids,) = self.gindex(l, r)
        # 伝播される区間のindexについて上から下に遅延配列の値を処理
        self.propagates(*ids)
        l += self.num
        r += self.num
        # 区間 [l,r)でdataとlazyをそれぞれ更新
        while l < r:
            if l & 1:
                self.lazy[l] = x
                self.tree[l] = x
                l += 1
            if r & 1:
                self.lazy[r - 1] = x
                self.tree[r - 1] = x
            r >>= 1
            l >>= 1
        # 伝播させた区間からはじめて下から上に処理
        for i in ids:
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def query(self, l, r):
        """
        [l,r)でsegfuncに相当するものを探索: Range Minimum Query
        """
        # 伝播される区間のindexについて上から下に遅延配列の値を処理
        # ids = self.gindex(l, r)
        self.propagates(*self.gindex(l, r))
        # 探索
        # 一致していたらその葉の値を返す
        if l == r:
            return self.tree[self.num + l]
        # 返却値の初期値を取得
        res = self.ide_ele
        l += self.num
        r += self.num
        # segfuncと同じ
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res


N, Q = [int(_) for _ in input().split()]
st = LazySegTree([ide_ele] * N, segfunc, ide_ele)
ans = []
for _ in range(Q):
    t, *q = [int(_) for _ in input().split()]
    if t == 0:
        s, t, x = q
        st.update(s, t + 1, x)
    else:
        s, t = q
        m = st.query(s, t + 1)
        ans.append(str(m))

print(*ans, sep="\n")

