N = int(input())
A = list(map(int, input().split()))
ans = 0
minA = abs(A[0])
neg = 0
for a in A:
    if a < 0:
        neg += 1
    ans += abs(a)
    minA = min(minA, abs(a))
if neg % 2 == 0:
    print(ans)
else:
    print(ans - 2 * minA)
