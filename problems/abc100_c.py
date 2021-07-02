N = int(input())
A = [int(_) for _ in input().split()]
ans = 0
for a in A:
    while a % 2 == 0:
        a = a // 2
        ans += 1
print(ans)