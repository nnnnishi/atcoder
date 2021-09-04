# 文字のN進数
import string

S = list(input())
K = int(input())

d = {}
d2s = {}
for i, s in enumerate(string.ascii_lowercase):
    d[s] = i
    d2s[i] = s

ans = ""
N = len(S)
for i in range(N):
    if i == N - 1:
        ans += d2s[(d[S[i]] + K) % 26]
    elif d[S[i]] == 0:
        ans += "a"
        continue
    elif K >= 26 - d[S[i]]:
        K -= 26 - d[S[i]]
        ans += "a"
    else:
        ans += S[i]
print(ans)
