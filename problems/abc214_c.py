N = int(input())
s = list(map(int, input().split()))
t = list(map(int, input().split()))
ds = s + s
dt = t + t
for i in range((2 * N) - 1):
    if dt[i + 1] >= dt[i] + ds[i]:
        dt[i + 1] = dt[i] + ds[i]

for i in range(N):
    print(min(dt[i], dt[i + N]))
