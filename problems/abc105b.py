N = int(input())
A = [int(_) for _ in input().split()]

min_ans = 10 ** 9 + 1
max_ans = 1
for i in range(N):
    max_ans = max(max_ans, A[i])
    min_ans = min(min_ans, A[i])
print(max_ans - min_ans)