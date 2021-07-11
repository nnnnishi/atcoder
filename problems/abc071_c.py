N = int(input())
a = [int(_) for _ in input().split()]
a.sort(reverse=True)
c = 0
b = -1
fa = -1
fb = -1
for ai in a:
    if ai != b:
        c = 1
        b = ai
    else:
        c += 1
        if c == 2:
            if fa == -1:
                fa = ai
                c = 0
                b = -1
            else:
                fb = ai
                exit(print(fb * fa))
print(0)
