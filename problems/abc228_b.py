N, X = list(map(int, input().split()))
A = [int(_) for _ in input().split()]
B = set()
ans = 1
while X - 1 not in B:
    B.add(X - 1)
    X = A[X - 1]
print(len(B))
