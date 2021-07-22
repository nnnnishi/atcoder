from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge

N, K = [int(_) for _ in input().split()]
l = []
for i in range(N):
    a, b = [int(_) for _ in input().split()]
    l.append([a, b])
heapify(l)
c = 0
t = 0
for _ in range(K):
    a, b = heappop(l)
    t += a
    c += 1
    heappush(l, [a + b, b])
print(t)
