N = int(input())
S1 = [0] * N
S2 = [0] * N
for i in range(N):
    C, P = [int(_) for _ in input().split()]
    if C == 1:
        S1[i] = P
    else:
        S2[i] = P

for i in range(1, N):
    S1[i] += S1[i - 1]
    S2[i] += S2[i - 1]

Q = int(input())
for _ in range(Q):
    A, B = [int(_) for _ in input().split()]
    if A == 1:
        print(S1[B - 1], S2[B - 1])
    else:
        print(S1[B - 1] - S1[A - 2], S2[B - 1] - S2[A - 2])

