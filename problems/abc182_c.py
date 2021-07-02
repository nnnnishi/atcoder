N = int(input())
S = list(str(N))
l = len(S)


def has_bit(n, s):
    return (n & 1 << s) > 0


ans = 20
for n in range(1 << l):
    c = ""
    for j in range(l):
        if has_bit(n, j):
            c += S[j]
    if len(c) > 0:
        if int(c) % 3 == 0:
            ans = min(l - len(c), ans)
if ans == 20:
    print(-1)
else:
    print(ans)
