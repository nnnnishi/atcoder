A, B = list(map(int, input().split()))
if B - A <= 0:
    print(0)
else:
    print(B - A + 1)
