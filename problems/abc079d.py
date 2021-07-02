H, W = [int(_) for _ in input().split()]
c = [[int(_) for _ in input().split()] for i in range(10)]
A = [[int(_) for _ in input().split()] for i in range(H)]

# ワーシャルフロイド
for k in range(10):
    for i in range(10):
        for j in range(10):
            c[i][j] = min(c[i][j], c[i][k] + c[k][j])

ans = 0
for y in range(H):
    for x in range(W):
        if A[y][x] == -1:
            continue
        else:
            ans += c[A[y][x]][1]
print(ans)