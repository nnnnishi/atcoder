N = int(input())
a = [int(_) for _ in input().split()]
b = [0] * N
ans_n = 0
ans = []
for i in range(N - 1, -1, -1):
    idx = i + 1
    d = N // idx
    c = 0
    for j in range(1, d):
        # print(i, idx, j, d)
        c += b[i + idx * j]
    if c % 2 != a[i]:
        b[i] = 1
        ans_n += 1
        ans.append(idx)
if ans_n == 0:
    print(ans_n)
else:
    print(ans_n)
    print(*ans)

