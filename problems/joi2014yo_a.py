ans = 0
for i in range(5):
    N = int(input())
    if N <= 40:
        ans += 40
    else:
        ans += N
print(ans // 5)
