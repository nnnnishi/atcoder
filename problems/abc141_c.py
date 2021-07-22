N, K, Q = [int(_) for _ in input().split()]
a = [K] * N
for i in range(Q):
    p = int(input())
    a[p - 1] += 1
for i in range(N):
    if a[i] - Q > 0:
        print("Yes")
    else:
        print("No")
