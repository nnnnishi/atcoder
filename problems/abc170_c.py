X, N = [int(_) for _ in input().split()]
if N == 0:
    exit(print(X))
p = [int(_) for _ in input().split()]
f = set(p)
m = 1000
ans = 0
for i in range(-1, 102):
    if i not in f:
        if abs(X - i) < m:
            ans = i
            m = abs(X - i)
print(ans)
