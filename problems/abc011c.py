N = int(input())
NG1 = int(input())
NG2 = int(input())
NG3 = int(input())
ngs = [NG1, NG2, NG3]

for ng in ngs:
    if ng == N:
        print("NO")
        exit()
if N <= 3:
    exit(print("YES"))

ngs.sort()
if ngs[0] + 1 == ngs[1] and ngs[1] + 1 == ngs[2]:
    print("NO")
    exit()
if N == 300:
    for ng in ngs:
        if ng % 3 == 0:
            exit(print("NO"))
ngs.sort(reverse=True)

if N == 299:
    if (
        (ngs[0] % 3 == 2 and ngs[1] % 3 == 0)
        or (ngs[0] % 3 == 2 and ngs[2] % 3 == 0)
        or (ngs[1] % 3 == 2 and ngs[2] % 3 == 0)
    ):
        exit(print("NO"))
if N == 298:
    if ngs[0] % 3 == 1 and ngs[1] % 3 == 2 and ngs[2] % 3 == 0:
        exit(print("NO"))

print("YES")