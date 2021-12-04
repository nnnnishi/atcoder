N = input()
nl = list(N)
n = len(N)

ans = 0
for mul in range(n):
    slow = "1" * mul + "1"
    sup = "1" * mul + "2"
    for d in range(n):
        low = int(slow)
        up = int(sup)
        low = low * (10 ** d)
        up = up * (10 ** d)
        if up <= int(N):
            ans += up - low
        else:
            if int(N) >= low:
                ans += int(N) - low + 1

print(ans)
