X = int(input())
for a in range(1, 10 ** 8):
    for b in range(a - 1, -(10 ** 8), -1):
        if pow(a, 5) - pow(b, 5) == X:
            print(a, b)
            exit()
        elif pow(a, 5) - pow(b, 5) > X:
            break
