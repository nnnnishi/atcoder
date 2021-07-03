N = int(input())
q = []
ans = []
for i in range(N - 1):
    q.append([int(_) for _ in input().split()])

# 開始
for i in range(N):
    t = 0
    for j in range(i, N - 1):
        s = q[j][1]
        f = q[j][2]
        c = q[j][0]
        # 時刻
        k = -(-max(s, t) // f)
        t = k * f + c
    print(t)
