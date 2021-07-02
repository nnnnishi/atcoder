N = int(input())
S = list(input())
ans = 0
for i in range(1000):
    check = list(str(i).zfill(3))
    k = 0
    for s in S:
        if k < 3 and check[k] == s:
            k += 1
    if k == 3:
        ans += 1
print(ans)