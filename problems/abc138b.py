N = int(input())
A = list(map(int, input().split()))
bo = 0
for i in range(N):
    bo += 1 / A[i]
print(1 / bo)
