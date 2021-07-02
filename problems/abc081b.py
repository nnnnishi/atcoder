N = int(input())
s = list(map(int, input().split()))
OK = True
ans = 0
while OK:
    for i in range(N):
        if s[i] % 2 != 0:
            OK = False
            break
        else:
            s[i] = s[i] // 2

    if OK:
        ans += 1
print(ans)
