from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
import heapq
from itertools import accumulate, product, permutations, combinations

# V: 頂点数
# G[v] = [w, ...]:
#    有向グラフ上の頂点vから到達できる頂点w
# deg[v]:
#    頂点vに到達できる頂点の数


V, M = [int(_) for _ in input().split()]

outs = defaultdict(list)
ins = defaultdict(int)
for _ in range(M):
    v1, v2 = [int(_) for _ in input().split()]
    outs[v1].append(v2)
    ins[v2] += 1

q = deque(v1 for v1 in range(1, V + 1) if ins[v1] == 0)
ans = []
h = []
while q or h:
    for _ in range(len(q)):
        heappush(h, q.popleft())
    m = heappop(h)
    ans.append(m)
    for v2 in outs[m]:
        ins[v2] -= 1
        if ins[v2] == 0:
            q.append(v2)
if len(ans) == V:
    print(*ans)
else:
    print(-1)
