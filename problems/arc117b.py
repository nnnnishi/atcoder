N = int(input())
A = list(set(list(map(int, input().split()))))
A.sort()
n = len(A)
M = 10 ** 9 + 7
ans = 1
tmp = 0
for i in range(n):
    ans = (ans * (A[i] - tmp + 1)) % M
    tmp = A[i]
print(ans)