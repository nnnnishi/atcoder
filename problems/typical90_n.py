N = int(input())
A = [int(_) for _ in input().split()]
B = [int(_) for _ in input().split()]

A.sort()
B.sort()
ans = 0
for i in range(N):
    ans += abs(A[i] - B[i])
print(ans)