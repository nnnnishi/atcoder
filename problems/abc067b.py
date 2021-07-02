N, K = [int(_) for _ in input().split()]
L = [int(_) for _ in input().split()]

L.sort(reverse=True)
print(sum(L[:K]))