from scipy.special import comb

A, B, K = list(map(int, input().split()))
ans = ""
cnt = 0
while A + B >= 2:
    check = comb(A + B - 1, A - 1, exact=True)
    if K <= check:
        ans += "a"
        A -= 1
    else:
        ans += "b"
        K -= check
        B -= 1


if A == 1:
    ans += "a"
else:
    ans += "b"
print(ans)