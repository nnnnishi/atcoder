N = int(input())
if N == 1:
    print(1)
    exit()

b1 = int(input())
b2 = int(input())
if b2 - b1 < 0:
    d = "down"
elif b2 - b1 > 0:
    d = "up"

if N == 2:
    print(2)
    exit()

ans = 1
cnt = 1

b = b2
for _ in range(N - 2):
    h = int(input())
    if d == "down":
        if h < b:
            cnt += 1
        else:
            ans = max(ans, cnt + 1)
            cnt = 1
            d = "up"
    elif d == "up":
        if h > b:
            cnt += 1
        else:
            cnt += 1
            d = "down"
    b = h
ans = max(ans, cnt + 1)
print(ans)
