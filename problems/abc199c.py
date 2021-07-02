N = int(input())
S = list(input())
Q = int(input())
flip = False
for i in range(Q):
    T, A, B = list(map(int, input().split()))
    if T == 2:
        if flip:
            flip = False
        else:
            flip = True
    else:
        if not flip:
            sA = S[A - 1]
            sB = S[B - 1]
            S[A - 1] = sB
            S[B - 1] = sA
        else:
            if A - 1 < N and B - 1 < N:
                sA = S[A - 1 + N]
                sB = S[B - 1 + N]
                S[A - 1 + N] = sB
                S[B - 1 + N] = sA
            elif A - 1 >= N and B - 1 < N:
                sA = S[A - 1 - N]
                sB = S[B - 1 + N]
                S[A - 1 - N] = sB
                S[B - 1 + N] = sA
            elif A - 1 < N and B - 1 >= N:
                sA = S[A - 1 + N]
                sB = S[B - 1 - N]
                S[A - 1 + N] = sB
                S[B - 1 - N] = sA
            elif A - 1 >= N and B - 1 >= N:
                sA = S[A - 1 - N]
                sB = S[B - 1 - N]
                S[A - 1 - N] = sB
                S[B - 1 - N] = sA
if flip:
    print("".join(S[N:] + S[:N]))
else:
    print("".join(S))
