N = int(input())

Q = []
for _ in range(N):
    Q.append(int(input()))
G = [0] * N
# 初期化
start = Q[0]
before = Q[0]
idx = 0
G[idx] = 1

for i in range(1, N):
    # 同じ
    if before == Q[i]:
        G[idx] += 1
    # 異なる
    else:
        # 偶数
        if (i + 1) % 2 == 0:
            if idx == 0:
                G[idx] += 1
                start = Q[i]
                before = Q[i]
            else:
                G[idx - 1] += G[idx] + 1
                G[idx] = 0
                idx -= 1
                before = Q[i]
        # 奇数
        else:
            idx += 1
            G[idx] = 1
            before = Q[i]
ans = 0
if start == 0:
    for i in range(0, N, 2):
        ans += G[i]
else:
    for i in range(1, N, 2):
        ans += G[i]
print(ans)
