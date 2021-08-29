# 二部の最大マッチング
# scipyでmaxflowをとく
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csgraph.maximum_flow.html

from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import maximum_flow
import numpy as np


N = int(input())
# 赤い点
r = []
for _ in range(N):
    x, y = [int(_) for _ in input().split()]
    r.append([x, y])
# 青い点
b = []
for _ in range(N):
    x, y = [int(_) for _ in input().split()]
    b.append([x, y])


# 始点を0、終点を2N+1、赤を1...N,青を(N+1)...2Nとする
mat = np.zeros((2 * N + 2, 2 * N + 2))

# 赤から青への有向グラフを作る
for i in range(N):
    for j in range(N):
        # 赤が青よりx,y座標がともに小さいとき、つなげる
        if r[i][0] < b[j][0] and r[i][1] < b[j][1]:
            mat[i + 1][j + (N + 1)] = 1

# 始点と赤をつなぐ
for i in range(1, N + 1):
    mat[0][i] = 1

# 青と終点をつなぐ
for j in range(N + 1, 2 * N + 1):
    mat[j][2 * N + 1] = 1

# ライブラリを使うためにintegerにする
graph = csr_matrix(np.array(mat, dtype="int64"))
# 0から2*N+1まで
print(maximum_flow(graph, 0, 2 * N + 1).flow_value)
