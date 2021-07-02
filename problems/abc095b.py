N, X = [int(_) for _ in input().split()]
m = [int(input()) for i in range(N)]
sumX = sum(m)
minX = min(m)
print(len(m) + (X - sumX) // minX)
