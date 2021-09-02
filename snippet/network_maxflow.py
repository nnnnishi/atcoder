# 最小カットの最適解の目的関数値 = 最大流問題の最適解の目的関数値
# scipyでmaxflowをとく
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csgraph.maximum_flow.html

from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import maximum_flow
import numpy as np


N, G, E = [int(_) for _ in input().split()]
# 複数の終点をもつため、1つの終点tに集約する
mat = np.zeros((N + 1, N + 1))
p = [int(_) for _ in input().split()]

# 友達間の関係
for _ in range(E):
    a, b = [int(_) for _ in input().split()]
    mat[a][b] = 1
    mat[b][a] = 1

# 終点が複数なので集約

for pi in p:
    mat[pi][N] = 1
    mat[N][pi] = 1

# ライブラリを使うためにintegerにする
graph = csr_matrix(np.array(mat, dtype="int64"))
print(maximum_flow(graph, 0, N).flow_value)
