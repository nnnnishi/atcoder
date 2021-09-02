N, K = [int(_) for _ in input().split()]
s = []
for i in range(N):
    a, b = [int(_) for _ in input().split()]
    s += [a - b, b]
s.sort(reverse=True)
print(sum(s[:K]))
