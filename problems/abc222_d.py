N = int(input())
a = [int(_) for _ in input().split()]
b = [int(_) for _ in input().split()]
M = 998244353


ans = [0] * 3001

for j in range(a[0], b[0] + 1):
    ans[j] = 1

bs = a[0]
bt = b[0]
for i in range(1, N):
    s = a[i]
    t = b[i]
    cnt = 0
    if bt < s:
        for j in range(bs, bt + 1):
            cnt += ans[j]
            ans[j] = 0
            ans[j] %= M
        for j in range(s, t + 1):
            ans[j] += cnt
            ans[j] %= M
    else:
        for j in range(bs, s):
            cnt += ans[j]
            ans[j] = 0
            ans[j] %= M
        for j in range(s, bt + 1):
            ans[j] = cnt + ans[j]
            cnt = ans[j]
            ans[j] %= M
        for j in range(bt, t + 1):
            ans[j] = cnt
            ans[j] %= M
    bs = s
    bt = t
print(sum(ans) % M)
