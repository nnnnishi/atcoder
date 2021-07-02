N = int(input())
A = list(map(int, input().split()))
ans = 10 ** 20
for i in range(2 ** (N - 1)):
    cur = A[0]
    tot = 0
    for j in range(1, N):
        # xor
        if (i >> (N - 1) - j) & 1:
            tot ^= cur
            cur = A[j]
        else:
            # or
            cur |= A[j]
    tot ^= cur
    ans = min(ans, tot)
print(ans)
