N = int(input())
A = list(map(int, input().split()))

A.sort()
ok = True
for i in range(N - 1):
    if A[i] == A[i + 1]:
        ok = False
        break
if ok:
    print("YES")
else:
    print("NO")
