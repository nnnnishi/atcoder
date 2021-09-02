import math

T = int(input())
L, X, Y = [int(_) for _ in input().split()]
Q = int(input())
q = []
r = L / 2
for _ in range(Q):
    q.append(int(input()))
for t in q:
    e = 2 * math.pi * (t % T) / T
    bs = r - r * math.cos(e)
    bb = math.sqrt(((Y + r * math.sin(e)) ** 2) + (X ** 2))
    print(math.degrees(math.atan2(bs, bb)))
