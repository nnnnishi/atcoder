X, K, D = [int(_) for _ in input().split()]
X = abs(X)
if X - K * D >= 0:
    exit(print(X - K * D))
# Xをこえる値
N = X // D + 1
# 超える値からの残りが奇数
if (K - N) % 2 == 1:
    print(abs(X - N * D + D))
else:
    print(abs(X - N * D))
