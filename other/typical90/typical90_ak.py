import math


def segfunc(x, y):
    return max(x, y)


class SegTree:
    def __init__(self, init_val, segfunc, ide_ele):
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def add(self, k, x):
        k += self.num
        self.tree[k] += x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def update(self, k, x):
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
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


W, N = [int(_) for _ in input().split()]
dp = [[-1] * (W + 1) for i in range(N + 1)]
dp[0][0] = 0

for i in range(1, N + 1):
    il, ir, iv = [int(_) for _ in input().split()]
    # セグ木
    st = SegTree(dp[i - 1], segfunc, -math.inf)
    # おもみ
    for w in range(W + 1):
        # 区間
        if 0 <= w - il <= W and 0 <= w - ir <= W:
            c = st.query(w - ir, w - il + 1)
            if c >= 0:
                dp[i][w] = max(dp[i - 1][w], c + iv)
        elif 0 <= w - il <= W:
            c = st.query(0, w - il + 1)
            if c >= 0:
                dp[i][w] = max(dp[i - 1][w - 1], c + iv)
        elif 0 <= w - ir <= W:
            c = st.query(w - ir, W + 1)
            if c >= 0:
                dp[i][w] = max(dp[i - 1][w - 1], c + iv)
        dp[i][w] = max(dp[i - 1][w], dp[i][w])
    # print(dp[i])

print(dp[N][W])
