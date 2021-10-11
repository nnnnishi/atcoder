N, M = list(map(int, input().split()))
X = []
s = []
for i in range(N * 2):
    X.append(list(input()))
    s.append([0, i])
# print(X)


def judge(a, b):
    if a == "G":
        if b == "C":
            return 1
        else:
            return 0
    if a == "C":
        if b == "P":
            return 1
        else:
            return 0
    if a == "P":
        if b == "G":
            return 1
        else:
            return 0


for i in range(M):
    # たいせんあいてきめる
    s.sort(key=lambda x: (-x[0], x[1]))
    for j in range(N):
        # print(s[j * 2])
        t1 = s[j * 2][1]
        t2 = s[j * 2 + 1][1]
        if judge(X[t1][i], X[t2][i]):
            s[j * 2][0] += 1
        if judge(X[t2][i], X[t1][i]):
            s[j * 2 + 1][0] += 1

s.sort(key=lambda x: (-x[0], x[1]))
for i in range(2 * N):
    print(s[i][1] + 1)
