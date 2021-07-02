N = list(map(int, input().split()))
ans = 0
for n in N:
    ans += 7 - n
print(ans)