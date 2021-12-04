N = int(input())
c = []
for i in range(N):
    c.append(list(map(int, input().split())))
c.sort()
ans = 0
for i1 in range(N):
    for i2 in range(i1 + 1, N):
        for i3 in range(i2 + 1, N):
            A = c[i3][1] - c[i1][1]
            if (c[i2][0] - c[i1][0]) == 0:
                # i2とi1が重複しない
                if (c[i2][1] - c[i1][1]) != 0:
                    # i3とi1のy重複しない
                    if c[i1][0] != c[i3][0]:
                        ans += 1
            else:
                B = (c[i2][1] - c[i1][1]) * (c[i3][0] - c[i1][0])
                if A * (c[i2][0] - c[i1][0]) != B:
                    ans += 1
print(ans)
