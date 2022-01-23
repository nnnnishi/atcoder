K = int(input())
ans = 0
for i in range(1, K + 1):
    for j in range(i, K + 1):
        if i * j > K:
            break
        for k in range(j, K + 1):
            mul = i * j * k
            if mul <= K:
                n = len(set([i, j, k]))
                if n == 1:
                    ans += 1
                elif n == 2:
                    ans += 3
                else:
                    ans += 6
            elif mul > K:
                break
print(ans)
