N = int(input())
A = [int(_) for _ in input().split()]
cand = set(A)
ans = 0
for c in cand:
    t = 0
    for i in range(N):
        if A[i] >= c:
            t += c
        else:
            ans = max(t, ans)
            t = 0
    ans = max(t, ans)
print(ans)