import sys

input = sys.stdin.readline
N, W = [int(_) for _ in input().split()]
l = [0] * (2 * (10 ** 5) + 1)
for _ in range(N):
    s, t, p = [int(_) for _ in input().split()]
    l[s] += p
    l[t] -= p

for i in range(1, 2 * (10 ** 5) + 1):
    l[i] += l[i - 1]
# print(l[:100])
for li in l:
    if li > W:
        print("No")
        exit()
print("Yes")
