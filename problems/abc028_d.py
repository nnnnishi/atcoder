N, K = [int(_) for _ in input().split()]
tot = pow(N, 3)
# 3つおなじ
cnt = 1
# 2つおなじ
cnt += (N - 1) * 3
# 3つ違う
cnt += (K - 1) * (N - K) * 3 * 2
print(cnt / tot)
