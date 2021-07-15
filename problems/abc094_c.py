N = int(input())
X = [int(_) for _ in input().split()]
org = X.copy()
X.sort()

left = X[(N // 2) - 1]
right = X[N // 2]
for i in range(N):
    if org[i] <= left:
        print(right)
    else:
        print(left)
