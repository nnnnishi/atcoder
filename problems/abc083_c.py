a, b = [int(_) for _ in input().split()]
t = a
ans = 0
while t <= b:
    ans += 1
    t = t * 2
print(ans)
