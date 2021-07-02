from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

H, W, N = [int(_) for _ in input().split()]
A = []
for i in range(H):
    A.append(list(input()))
for sy, sx in product(range(H), range(W)):
    if A[sy][sx] == "S":
        x = sx
        y = sy
        break


ans = 0
for i in range(1, N + 1):
    finding = True
    for cy, cx in product(range(H), range(W)):
        if A[cy][cx] == "-":
            A[cy][cx] = "."
    # 幅優先
    Q = deque()
    Q.append([y, x, 0])
    while len(Q) > 0 and finding:
        y1, x1, c = Q.popleft()
        # print(y1, x1, c)
        # うえ、した、みぎ、ひだり
        for y2, x2 in [[y1 + 1, x1], [y1 - 1, x1], [y1, x1 + 1], [y1, x1 - 1]]:
            if 0 <= x2 <= W - 1 and 0 <= y2 <= H - 1 and A[y2][x2] not in ["X", "-"]:
                if A[y2][x2] != str(i):
                    Q.append([y2, x2, c + 1])
                    if A[y2][x2] == ".":
                        A[y2][x2] = "-"
                else:
                    c += 1
                    finding = False
                    break
    y, x = y2, x2
    ans += c
print(ans)