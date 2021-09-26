N, H = [int(_) for _ in input().split()]
A = []
B = []
for i in range(N):
    a, b = [int(_) for _ in input().split()]
    A.append(a)
    B.append(b)
x = max(A)
B.sort(reverse=True)
ans = 0
for i in range(N):
    if B[i] > x:
        H -= B[i]
        ans += 1
        if H <= 0:
            exit(print(ans))
    else:
        ans += -(-H // x)
        exit(print(ans))
ans += -(-H // x)
exit(print(ans))

