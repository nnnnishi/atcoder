class Bit:
    """
    Bit(n+1):配列数nで初期化
    sum(i):a_0 - a_i の最大値を取得
    add(i, x): a_iをxで更新する
    """

    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

    def sum(self, i):
        s = -(10 ** 18)  # -INF
        while i > 0:
            s = max(s, self.tree[i])
            i -= i & -i
        return s

    def add(self, i, x):
        while i <= self.size:
            self.tree[i] = max(x, self.tree[i])
            i += i & -i