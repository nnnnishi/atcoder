# https://qiita.com/takayg1/items/c811bd07c21923d7ec69
# https://atcoder.jp/contests/abc185/tasks/abc185_f
# セグメント木の解説
# https://tsutaj.hatenablog.com/entry/2017/03/29/204841
##### segfunc #####
def segfunc(x, y):
    return min(x, y)


#####ide_ele 初期値#####
ide_ele = 2 ** 31 - 1


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
        # 二分木の葉として必要な要素数
        self.num = 1 << (n - 1).bit_length()
        # セグメント木を作成
        self.tree = [ide_ele] * 2 * self.num
        # 配列の値を葉にセット
        for i in range(n):
            # 葉の部分を初期値でうめる
            self.tree[self.num + i] = init_val[i]
        # 葉よりうえの木をうめてく
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
        # 葉のindexは self.num + k
        k += self.num
        self.tree[k] = x
        # いちばん上まで登りながら更新
        while k > 1:
            # k>>1は k//2 の操作、k^1はkの隣のindex (if k = even k+1 else k)
            # 隣と比較してsegfuncのものを上に適用する
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            # 上に登る
            k >>= 1

    def query(self, l, r):
        """
        [l, r)のsegfuncしたものを得る
        l: index(0-index)
        r: index(0-index)
        """
        # 返却値の初期値を取得
        res = self.ide_ele
        # 木の葉のlとrのindexを取得
        l += self.num
        r += self.num
        # lとrの値が一致するまで登りながら所属するブロックの最小値を取得していく
        while l < r:
            # lが奇数
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                # l+=1して偶数にする
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            # l,rを//2して上に登る
            l >>= 1
            r >>= 1
        return res


N, Q = [int(_) for _ in input().split()]
A = [ide_ele] * N
st = SegTree(A, segfunc, ide_ele)
for _ in range(Q):
    c, x, y = [int(_) for _ in input().split()]
    if c == 0:
        # iは0-index
        i, val = x, y
        st.update(i, val)
    else:
        l, r = x, y
        # iは0-index,右端開区間なので+1まで
        m = st.query(l, r + 1)
        print(m)
