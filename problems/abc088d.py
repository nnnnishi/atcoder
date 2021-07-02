from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

H, W = list(map(int, input().split()))
A = []
ok = 0
for i in range(H):
    A.append(list(input()))
    ok += A[i].count(".")
ans = 0
visited = [[-1] * W for y in range(H)]
q = deque()
q.append((0, 0))
visited[0][0] = 0
while q:
    y, x = q.popleft()
    for ny, nx in [[y - 1, x], [y, x - 1], [y + 1, x], [y, x + 1]]:
        if (
            0 <= ny <= H - 1
            and 0 <= nx <= W - 1
            and visited[ny][nx] == -1
            and A[y][x] != "#"
        ):
            visited[ny][nx] = visited[y][x] + 1
            q.append((ny, nx))

if visited[H - 1][W - 1] == -1:
    print(-1)
else:
    print(ok - visited[H - 1][W - 1] - 1)
