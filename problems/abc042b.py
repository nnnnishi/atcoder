N, L = [int(_) for _ in input().split()]
S = []
for i in range(N):
    S.append(input())
S.sort()
print(*S, sep="")
