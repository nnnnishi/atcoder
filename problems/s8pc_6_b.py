N = int(input())
A = []
B = []
dis = 0
for i in range(N):
    a, b = [int(_) for _ in input().split()]
    A.append(a)
    B.append(b)
    dis += b - a
ans = 10 ** 100
for i in range(N):
    for j in range(N):
        en = A[i]
        ou = B[j]
        tmp_ans = dis
        for k in range(N):
            tmp_ans += abs(en - A[k])
            tmp_ans += abs(ou - B[k])
        ans = min(ans, tmp_ans)
print(ans)
