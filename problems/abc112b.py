N, T = [int(_) for _ in input().split()]
ans = 10000
for i in range(N):
    c, t = [int(_) for _ in input().split()]
    if t <= T:
        ans = min(ans, c)
if ans == 10000:
    print("TLE")
else:
    print(ans)