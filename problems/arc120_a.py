N = int(input())
A = [int(_) for _ in input().split()]
ma = [0] * N
cumA = [0] * N
mx = 0
for i in range(N):
    if i > 0:
        cumA[i] += cumA[i - 1] + A[i]
    if A[i] > mx:
        mx = A[i]
    ma[i] = mx + A[0]
print(ma[0])
pre = 0
for i in range(1, N):
    pre += cumA[i]
    print((i + 1) * ma[i] + pre)
