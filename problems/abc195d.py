N, M, Q = list(map(int, input().split()))
G = []
for i in range(N):
    w, v = list(map(int, input().split()))
    G.append((v, w))
G.sort(key=lambda l: (-l[0], l[1]))
X = [0] + list(map(int, input().split()))
query = []
for _ in range(Q):
    query.append(list(map(int, input().split())))
for L, R in query:
    X_use = [True] * (M + 1)
    ans = 0
    for g in G:
        tmp_X = 10 ** 6 + 1
        tmp_i = 0
        for i in [idx for idx in range(1, L)] + [idx for idx in range(R + 1, M + 1)]:
            if X_use[i]:
                if X[i] >= g[1]:
                    if min(tmp_X, X[i]) == X[i]:
                        tmp_i = i
                        tmp_X = X[i]
        if tmp_i != 0:
            X_use[tmp_i] = False
            ans += g[0]
    print(ans)
