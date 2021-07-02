s, c = [int(_) for _ in input().split()]

cnt = 0
a = min(s, c // 2)
s -= a
c -= a * 2
cnt += a
if c > 0:
    cnt += c // 4


print(cnt)
