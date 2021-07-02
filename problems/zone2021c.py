N = int(input())
p = []
max_s = 0
for i in range(N):
    pi = list(map(int, input().split()))
    max_s = max(max(pi), max_s)
    p.append(pi)


def check(num):
    pset = set()
    for pi in p:
        s_bit = 0
        for j in range(5):
            if pi[j] >= num:
                s_bit += 1 << j
        pset.add(s_bit)
    ok = False
    for a in pset:
        if not ok:
            for b in pset:
                if not ok:
                    for c in pset:
                        if not ok:
                            if (a | b | c) == (1 << 5) - 1:
                                ok = True
    return ok


# 二部探索
ok = 0
ng = max_s + 1
while ng - ok > 1:
    mid = (ng + ok) // 2
    if check(mid):
        ok = mid
    else:
        ng = mid
print(ok)
