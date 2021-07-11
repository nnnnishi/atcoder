import string

N = int(input())

d = {}
i = 0
for s in string.ascii_lowercase:
    d[i] = s
    i += 1
ans = ""
while N > 0:
    N -= 1
    ans += d[N % 26]
    N = N // 26
print(ans[::-1])
