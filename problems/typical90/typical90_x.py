N, K = [int(_) for _ in input().split()]
A = [int(_) for _ in input().split()]
B = [int(_) for _ in input().split()]

c = 0
for i in range(N):
    c += abs(A[i] - B[i])

if c > K:
    print("No")
else:
    if (K - c) % 2 == 0:
        print("Yes")
    else:
        print("No")
