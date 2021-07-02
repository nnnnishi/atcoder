N = int(input())
ans = 0
for i in range(1, N + 1, 2):
    cnt = 0
    for j in range(1, i + 1, 2):
        if j ** 2 < i:
            if i % j == 0:
                if i != j:
                    cnt += 2
                else:
                    cnt = 1
    if cnt == 8:
        ans += 1
print(ans)