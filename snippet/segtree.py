# https://qiita.com/takayg1/items/c811bd07c21923d7ec69
# https://atcoder.jp/contests/abc185/tasks/abc185_f
#####segfunc#####
def segfunc(x, y):
    return x ^ y


#################

#####ide_ele#####
ide_ele = 0
#################


class SegTree:
    """
    init(init_val, ide_ele): 配列init_valで初期化 O(N)
    update(k, x): k番目の値をxに更新 O(logN)
    query(l, r): 区間[l, r)をsegfuncしたものを返す O(logN)
    """

    def __init__(self, init_val, segfunc, ide_ele):
        """
        init_val: 配列の初期値
        segfunc: 区間にしたい操作
        ide_ele: 単位元
        n: 要素数
        num: n以上の最小の2のべき乗
        tree: セグメント木(1-index)
        """
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        # 配列の値を葉にセット
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        """
        k番目の値をxに更新
        k: index(0-index)
        x: update value
        木の中のl番目の要素に直接演算したいとき
        st.tree[l - 1 + (1 << (N - 1).bit_length())]
        """
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        """
        [l, r)のsegfuncしたものを得る
        l: index(0-index)
        r: index(0-index)
        """
        res = self.ide_ele

        l += self.num
        r += self.num
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
A = [int(_) for _ in input().split()]
st = SegTree(A, segfunc, 0)
for i in range(Q):
    t, l, r = [int(_) for _ in input().split()]
    if t == 1:
        st.update(l - 1, st.tree[l - 1 + (1 << (N - 1).bit_length())] ^ r)
    else:
        # 右開区間なのでrは+1
        m = st.query(l - 1, r)
        print(m)
