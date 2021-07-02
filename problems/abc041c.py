N = int(input())
A = [int(_) for _ in input().split()]
S = []
for i in range(N):
    S.append([A[i], i + 1])
S.sort(reverse=True)
for i in range(N):
    print(S[i][1])