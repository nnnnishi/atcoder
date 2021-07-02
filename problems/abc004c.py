N = int(input())
N = N % 30
i = N // 5 + 1  # 挿入する数字
j = N % 5  # 挿入する場所
k = (N // 5 + 1) % 6 + 1  # 最初の数字
ans = []
for idx in range(6):
    if idx == j:
        ans.append(i)
    if len(ans) < 6:
        ans.append((N // 5 + 1 + idx) % 6 + 1)
print("".join(map(str, ans)))
