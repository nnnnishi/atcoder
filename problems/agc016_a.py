# 文字のN進数
import string

X = input()
ans = 1000
for c in string.ascii_lowercase:
    sx = list(X)
    cnt = 0
    while len(set(list(sx))) > 1:
        cnt += 1
        for i in range(len(sx) - 1):
            if sx[i] == c or sx[i + 1] == c:
                sx[i] = c
        sx = sx[:-1]
    ans = min(cnt, ans)

print(ans)
