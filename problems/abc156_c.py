N = int(input())
x = [int(_) for _ in input().split()]
ans = 10 ** 10
for i in range(1, 101):
    tmp = 0
    for xi in x:
        tmp += (xi - i) ** 2
    ans = min(ans, tmp)
print(ans)