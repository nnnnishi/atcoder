from collections import defaultdict, Counter
import string

string.ascii_lowercase
defaultdict(int)

# 再帰用
import sys

sys.setrecursionlimit(1000000)

# itertools
import itertools
for x,y in itertools.product(range(101),repeat = 2):

# bit
def has_bit(n, s):
    return (n & 1 << s) > 0


# deque
from collections import deque

# 幅優先
Q = deque()
Q.append([sy - 1, sx - 1])
n[sy - 1][sx - 1] = 0
while len(Q) > 0:
    # 4辺チェックしキューへ追加
    i = Q.popleft()

# ダイクストラ
Q = [(0, 0)]
dist[0] = 0

while len(Q) > 0:
    d, i = heapq.heappop(Q)
    if done[i]:
        continue
    for g in graph[i]:
        j = g[1]
        c = g[0]
        if dist[j] == -1 or dist[j] > dist[i] + c:
            dist[j] = dist[i] + c
            heapq.heappush(Q, (dist[j], j))
    done[i] = True

# ワーシャルフロイド
for k in range(N):
    for i in range(N):
        for j in range(N):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

# 深さ優先
def dfs(i):
    global ans
    y = i[0]
    x = i[1]
    if y == gy and x == gx:
        ans = True
    v[y][x] = False
    for y2, x2 in [[y, x + 1], [y, x - 1], [y + 1, x], [y - 1, x]]:
        if 0 <= x2 < W and 0 <= y2 < H and v[y2][x2] == True:
            dfs([y2, x2])


# rotation
import numpy as np

N = int(input())
x0, y0 = list(map(int, input().split()))
x1, y1 = list(map(int, input().split()))

x = (x0 + x1) / 2
y = (y0 + y1) / 2


def rotation_o(u, t, deg=False):

    # 度数単位の角度をラジアンに変換
    if deg == True:
        t = np.deg2rad(t)

    # 回転行列
    R = np.array([[np.cos(t), -np.sin(t)], [np.sin(t), np.cos(t)]])

    return np.dot(R, u)


# ユークリッド距離
import numpy

x1 = 2
y1 = 2
x2 = 4
y2 = 6
a = numpy.array([x1, y1])
b = numpy.array([x2, y2])
u = b - a
numpy.linalg.norm(u)

# grid dykstra
def dykstra(y, x):
    dist = []
    for _ in range(H):
        dist.append([INF] * W)
    root = (y, x)
    dist[y][x] = 0
    # ダイクストラ
    Q = [(0, root)]
    while len(Q) > 0:
        d, i = heapq.heappop(Q)
        yi = i[0]
        xi = i[1]
        for yj, xj in [(yi + 1, xi), (yi - 1, xi), (yi, xi + 1), (yi, xi - 1)]:
            if (
                0 <= yj <= H - 1
                and 0 <= xj <= W - 1
                and dist[yj][xj] > dist[yi][xi] + A[yj][xj]
            ):
                dist[yj][xj] = dist[yi][xi] + A[yj][xj]
                heapq.heappush(Q, (dist[yj][xj], (yj, xj)))
    return dist


from functools import lru_cache
import sys

sys.setrecursionlimit(1000000)
@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

# エラトステネスの篩
# 1はじまりにする、0と1はFalse、N-1までの配列をつくる
is_prime = [False, False] + [True] * (N - 2)
for n in range(2, N):
    if is_prime[n]:
        check = n + n
        while check < N:
            is_prime[check] = False
            check += n
 
# Trueの数を数える
print(sum([1 for i in range(len(is_prime)) if is_prime[i]]))

# 約数列挙
def make_divisors(N):
    div_low = []
    div_high = []
    for i in range(1, N + 1):
        if i * i > N:
            break
        if N % i == 0:
            div_low.append(i)
            if i != N // i:
                div_high.append(N // i)

    div = div_low + div_high[::-1]

# combination N large
def cmb(n, r):
    if n - r < r:
        r = n - r
    if r == 0:
        return 1
    if r == 1:
        return n
    # 分子
    numerator = [n - r + k + 1 for k in range(r)]
    # 分母
    denominator = [k + 1 for k in range(r)]

    for p in range(2, r + 1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p - 1, r, p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return result

# 逆元 cmb
def cmb(n, r, mod):
    if r < 0 or r > n:
        return 0
    r = min(r, n - r)
    return g1[n] * g2[r] * g2[n - r] % mod


mod = (10 ** 9) + 7  # 出力の制限
n = 2 * (10 ** 6) + 1  # nの最大値
g1 = [1, 1]  # 元テーブル
g2 = [1, 1]  # 逆元テーブル
inverse = [0, 1]  # 逆元テーブル計算用テーブル

for i in range(2, n + 1):
    g1.append((g1[-1] * i) % mod)
    inverse.append((-inverse[mod % i] * (mod // i)) % mod)
    g2.append((g2[-1] * inverse[-1]) % mod)

# combination N small

from scipy.special import comb
a = comb(n, r, exact=True)

# 座標圧縮
def compress(arr):
    *XS, = set(arr)
    XS.sort()
    return {e: i for i, e in enumerate(XS)}

# unionfind
from collections import defaultdict

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())

N, M = [int(_) for _ in input().split()]
uf = UnionFind(N)
# 添字を変換
dic = {}
inv_dic = {}
for i in range(N):
    dic[i + 1] = i
    inv_dic[i] = i + 1

bridge = []
for i in range(M):
    bridge.append([int(_) for _ in input().split()])

for i in range(M):
    A, B = bridge[i]
    uf.union(dic[A], dic[B])

# 素因数分解
def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

# めぐる式二部探索

def is_ok(arg):
    # 条件を満たすかどうか？問題ごとに定義
    pass


def meguru_bisect(ng, ok):
    '''
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義すべし
    ng ok は  とり得る最小の値-1 とり得る最大の値+1
    最大最小が逆の場合はよしなにひっくり返す
    '''
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

# 最小公倍数
import math
def my_lcm(x, y):
    return (x * y) // math.gcd(x, y)

print(my_lcm(6, 4))

# 最小公約数
import math
math.gcd(x, y)
# 2つ以上の最小公約数
from functools import reduce

# 2つ以上の最小公倍数
def my_lcm_base(x, y):
    return (x * y) // math.gcd(x, y)

def my_lcm(*numbers):
    return reduce(my_lcm_base, numbers, 1)


# 2つ以上の最小公約数
def my_gcd(*numbers):
    return reduce(math.gcd, numbers)

# ベルマンフォード
# O(EV)
def bellman_ford(s):
    d = [float("inf")] * V  # 各頂点への最小コスト
    d[s] = 0  # 自身への距離は0
    for i in range(V):
        update = False  # 更新が行われたか
        # すべての辺をたどる
        for s, e, c in G:
            if d[e] > d[s] + c:
                d[e] = d[s] + c
                update = True
        if not update:
            break
        # V-1回以上更新できる場合は負閉路が存在
        if i == V - 1:
            exit(print("inf"))
    return d


V, M = [int(_) for _ in input().split()]
G = []
for _ in range(M):
    s, e, c = [int(x) for x in input().split()]  # 始点,終点,コスト
    # 0はじまりにする
    s -= 1
    e -= 1
    G.append([s, e, c])
    # g.append([e, s, c])  # 無向グラフは逆側もいれる
print(bellman_ford(0))

# 四捨五入
def my_round(val, digit=0):
    p = 10 ** digit
    return (val * p * 2 + 1) // 2 / p

Dis = my_round(Dis / 60, 1)
