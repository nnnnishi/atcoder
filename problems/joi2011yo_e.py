import bisect

D = int(input())
N = int(input())
M = int(input())
d = []
k = []
for i in range(N - 1):
    d.append(int(input()))
d += [0, D]
for i in range(M):
    k.append(int(input()))
d.sort()


def check(n):
    ok = 0
    ng = N
    if n == 0:
        return 0
    else:
        # nを超えない最大のdをもとめる
        while ng - ok > 1:
            mid = (ok + ng) // 2
            if n >= d[mid]:
                ok = mid
            else:
                ng = mid
        return min(abs(d[ok + 1] - n), abs(d[ok] - n))


def check_b(n):
    if n == 0:
        return 0
    idx = bisect.bisect_left(d, n)
    return min(abs(d[idx] - n), abs(d[idx - 1] - n))


ans = 0
for i in range(M):
    ans += check(k[i])
print(ans)