N, Q = [int(_) for _ in input().split()]
A = [int(_) for _ in input().split()]
B = [0] * N
s = 0
for i in range(1, N):
    B[i] = A[i] - A[i - 1]
    s += abs(B[i])
# リストを用意
for i in range(Q):
    L, R, V = [int(_) for _ in input().split()]
    L -= 1
    R -= 1
    if L >= 1 and R < N - 1:
        mae = abs(B[L]) + abs(B[R + 1])
        B[L] = B[L] + V
        B[R + 1] = B[R + 1] - V
        ato = abs(B[L]) + abs(B[R + 1])
        s = s + ato - mae
    elif L < 1 and R < N - 1:
        mae = abs(B[L]) + abs(B[R + 1])
        B[R + 1] = B[R + 1] - V
        ato = abs(B[L]) + abs(B[R + 1])
        s = s + ato - mae
    elif L >= 1 and R >= N - 1:
        mae = abs(B[L])
        B[L] = B[L] + V
        ato = abs(B[L])
        s = s + ato - mae
    print(s)
