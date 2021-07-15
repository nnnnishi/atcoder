N, K = [int(_) for _ in input().split()]
H = [int(_) for _ in input().split()]
H.sort(reverse=True)
print(sum(H[K:]))
