N, K = list(map(int, input().split()))
A = []
for i in range(N):
    A.append(sum([int(_) for _ in input().split()]))
B = A.copy()
A.sort(reverse=True)
P = A[K - 1]
Q = P - 300
for b in B:
    if b >= Q:
        print("Yes")
    else:
        print("No")

