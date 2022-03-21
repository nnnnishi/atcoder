N, A, B = list(map(int, input().split()))
P, Q, R, S = list(map(int, input().split()))
X = [["."] * (S - R + 1) for _ in range(Q - P + 1)]

for i in range(R, S + 1):
    for j in range(P, Q + 1):
        if i - j == B - A or j + i == A + B:
            X[j - P][i - R] = "#"

for i in range((Q - P + 1)):
    print("".join(X[i]))

