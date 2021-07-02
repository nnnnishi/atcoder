N = int(input())
C = []
for _ in range(N):
    C.append(int(input()))
ans = 0
for i in range(N):
    cnt = 0
    for j in range(N):
        if i != j:
            # C[j]がC[i]の約数
            if C[i] % C[j] == 0:
                cnt += 1
    # 確率をだす
    if (cnt + 1) % 2 == 0:
        ans += 0.5
    else:
        ans += (cnt + 2) / (2 * cnt + 2)
print(ans)
