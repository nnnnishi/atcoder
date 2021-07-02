import numpy as np
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge

K, N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
B = np.array(A) * (M / N)
Bint = np.round(B)
if sum(Bint) == M:
    print(*Bint.astype(int))
else:
    # へってるときは一番ふやしやすいのをふやす
    sa = B - Bint
    if M > sum(Bint):
        # 増やす数
        p = M - sum(Bint)
        h = []
        heapify(h)
        for i in range(K):
            if sa[i] >= 0:
                heappush(h, (1 - sa[i], i))
            else:
                heappush(h, (1 - sa[i], i))
        for _ in range(int(np.round(p))):
            q = heappop(h)
            Bint[q[1]] += 1
        print(*Bint.astype(int))
    # ふえてるときは一番減らしやすいのをへらす
    else:
        # へらすかず
        p = sum(Bint) - M
        h = []
        heapify(h)
        for i in range(K):
            if sa[i] >= 0:
                heappush(h, (1 + sa[i], i))
            else:
                heappush(h, (sa[i] + 1, i))
        for _ in range(int(np.round(p))):
            q = heappop(h)
            Bint[q[1]] -= 1
        print(*Bint.astype(int))
