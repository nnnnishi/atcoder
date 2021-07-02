N = int(input())
ok = True
ans = 0
while ok:
    if 2 ** ans > N:
        ok = False
    else:
        ans += 1
print(2 ** (ans - 1))
