N = int(input())
a = [int(_) for _ in input().split()]
check = set()
for ai in a:
    while ai % 2 == 0:
        ai = ai // 2
    check.add(ai)
print(len(check))
