N = int(input())
v = [int(_) for _ in input().split()]
v.sort()
ans = v[0]
for i in range(1, N):
    ans = (ans + v[i]) / 2
print(ans)