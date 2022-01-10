import sys

# input = sys.stdin.readline
N = int(input())
A = [int(_) for _ in input().split()]
A.sort(reverse=True)
ans = 0
for i in range(N):
    # print(A[i] * (N - 1) - 2 * i)
    ans += A[i] * ((N - 1) - (2 * i))
print(ans)
