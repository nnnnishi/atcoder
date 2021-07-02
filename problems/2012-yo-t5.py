from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations


W, H = list(map(int, input().split()))
A = [[0] + [int(_) for _ in input().split()] + [0] for i in range(H)]
padd = [[0] * (W + 2)]
A = padd + A + padd
visited = [[False] * (W + 2) for _ in range(H + 2)]
norm = [[1, 0], [-1, 0], [0, 1], [0, -1]]
# odd:abno[1], even:abno[0]
abno = [[[-1, -1], [1, -1]], [[1, 1], [-1, 1]]]

q = deque()
q.append((0, 0))
visited[0][0] = True
ans = 0
while q:
    y, x = q.popleft()
    for dy, dx in norm + abno[y % 2]:
        if 0 <= y + dy <= H + 1 and 0 <= x + dx <= W + 1:
            if A[y + dy][x + dx] == 1:
                ans += 1
            else:
                if not visited[y + dy][x + dx]:
                    q.append((y + dy, x + dx))
                    visited[y + dy][x + dx] = True
print(ans)