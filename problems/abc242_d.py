import sys

input = sys.stdin.readline

S = input().rstrip().replace("A", "0").replace("B", "1").replace("C", "2")
S = list(map(int, list(S)))
Q = int(input())
for _ in range(Q):
    t, k = [int(_) for _ in input().split()]
    k -= 1
    # 最初の記号 X
    if t < 60:
        i = k // (1 << t)
        X = S[i]
        k = k - (i * (1 << t))
    else:
        X = S[0]
    # なんばんめ
    k2 = bin(k).count("1")
    k1 = t - k2
    Y = (X + (k1 % 3) + (k2 % 3) * 2) % 3
    if Y == 0:
        print("A")
    elif Y == 1:
        print("B")
    else:
        print("C")
