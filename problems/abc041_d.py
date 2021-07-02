N, M = [int(_) for _ in input().split()]
c = [[0] * N for i in range(N)]
for i in range(M):
    x, y = [int(_) for _ in input().split()]
    c[x - 1][y - 1] = True

dp = [0] * (1 << N)
# 空集合のときトポロジカルソートの方法は1つ
dp[0] = 1
# i はうさぎの集合
for i in range(1 << N):
    # 取り除くうさぎ
    for j in range(N):
        # うさぎが含まれない
        if not (i & (1 << j)):
            # いちばん右か
            ok = True
            # 他のうさぎkが含まれていてjへのびるものがあれば一番みぎでない
            for k in range(N):
                if i & (1 << k):
                    if c[k][j]:
                        ok = False
            if ok:
                # いちばんみぎなら足す
                dp[i | (1 << j)] += dp[i]

print(dp[(1 << N) - 1])
