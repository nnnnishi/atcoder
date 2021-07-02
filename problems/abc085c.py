N, Y = list(map(int, input().split()))
go_f = True
for b in range(N + 1):
    if go_f:
        for c in range(N + 1):
            if go_f:
                if N - b - c >= 0 and 10000 * (N - b - c) + 5000 * b + 1000 * c == Y:
                    print(N - b - c, b, c)
                    go_f = False
if go_f:
    print(-1, -1, -1)
