from itertools import accumulate, product, permutations, combinations

N, M = [int(_) for _ in input().split()]
edge = [input() for i in range(M)]
ans = 0


def has_bit(n, i):
    return n & (1 << i) > 0


for n in range(1, 1 << N):
    mem = []
    for i in range(N):
        if has_bit(n, i):
            mem.append(str(i + 1))
    ok = True
    for x in combinations(mem, 2):
        x = " ".join(x)
        if x not in edge:
            ok = False
            break
    if ok:
        ans = max(ans, len(mem))
print(ans)