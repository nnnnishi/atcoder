N = int(input())
A = [int(_) for _ in input().split()]
ans = 10 ** 30
for i in range(-100, 101):
    tmp = 0
    for a in A:
        tmp += (a - i) ** 2
    ans = min(ans, tmp)
print(ans)
