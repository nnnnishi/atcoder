N = int(input())
C = [4] * N
A = list(map(int, input().split()))
for a in A:
    C[a - 1] -= 1
for i in range(N):
    if C[i] != 0:
        print(i + 1)
        break
