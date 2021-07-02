N, M = [int(_) for _ in input().split()]
# bit
def has_bit(n, i):
    return (n & 1 << i) > 0


C = []
for i in range(M):
    C.append([int(_) for _ in input().split()])

K = int(input())
D = []
for i in range(K):
    D.append([int(_) for _ in input().split()])

ans = 0
# K人が選ぶ組み合わせn
for n in range(1 << K):
    L = set()
    cnt = 0
    # 桁数
    for i in range(K):
        if has_bit(n, i):
            L.add(D[i][0])
        else:
            L.add(D[i][1])
    for a, b in C:
        if a in L and b in L:
            cnt += 1
    ans = max(ans, cnt)
print(ans)