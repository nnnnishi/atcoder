import sys

# input = sys.stdin.readline
N = int(input())
X = []
Y = []
for _ in range(N):
    x, y = [int(_) for _ in input().split()]
    X.append(x)
    Y.append(y)

X.sort(reverse=True)
Y.sort(reverse=True)
ans = 0
for i in range(N):
    # print(A[i] * (N - 1) - 2 * i)
    ans += X[i] * ((N - 1) - (2 * i))
    ans += Y[i] * ((N - 1) - (2 * i))
print(ans)
