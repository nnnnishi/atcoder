N = int(input())
H = []
S = []
maxH = 0
minH = 0
for i in range(N):
    h, s = list(map(int, input().split()))
    H.append(h)
    S.append(s)
    minH = max(h, minH)
    maxH = max(maxH, h + N * s)


def check(X):
    sec = []
    for i in range(N):
        sec.append((X - H[i]) // S[i])
    sec.sort()
    for i in range(N):
        if sec[i] < i:
            return False
    return True


ok = maxH + 1
ng = minH - 1
while abs(ok - ng) > 1:
    mid = (ng + ok) // 2
    if check(mid):
        ok = mid
    else:
        ng = mid
print(ok)