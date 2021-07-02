N, M = [int(_) for _ in input().split()]
S = [-1] * N
if N == 1 and M == 0:
    exit(print(0))

for i in range(M):
    s, c = [int(_) for _ in input().split()]
    if S[s - 1] != -1 and S[s - 1] != c:
        exit(print(-1))
    elif N != 1 and s == 1 and c == 0:
        exit(print(-1))
    else:
        S[s - 1] = c
for i in range(len(S)):
    if i == 0:
        if S[i] == -1:
            S[i] = 1
    else:
        if S[i] == -1:
            S[i] = 0
print(int("".join([str(s) for s in S])))
