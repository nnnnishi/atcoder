N = int(input())
check = set()
print(1, flush=True)
check.add(1)
res = int(input())
while res != 0:
    check.add(res)
    for i in range(1, 2 * N + 2):
        if i not in check:
            check.add(i)
            print(i, flush=True)
            break
    res = int(input())
