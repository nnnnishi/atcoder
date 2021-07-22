A, B, C = list(map(int, input().split()))
if B - A == C - B:
    exit(print(0))

if B - A >= 0:
    if C - B >= B - A:
        if (A + C) % 2 == 0:
            print(((A + C) // 2) - B)
        else:
            print(((A + 1 + C) // 2) - B + 1)
    else:
        print(2 * B - A - C)
else:
    if C - B <= B - A:
        print(2 * B - A - C)
    else:
        if (A + C) % 2 == 0:
            print(((A + C) // 2) - B)
        else:
            print(((A + 1 + C) // 2) - B + 1)
