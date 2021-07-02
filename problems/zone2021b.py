N, D, H = list(map(int, input().split()))
d = []
h = []
ans = 0
for i in range(N):
    di, hi = list(map(int, input().split()))
    tmp = hi - ((H - hi) * di) / (D - di)
    ans = max(tmp, ans)
print(ans)