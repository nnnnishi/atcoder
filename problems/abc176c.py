N = int(input())
ans = []
for i in range(1, N + 1):
    if N % i == 0:
        ans += [i, N // i]
    if i * i > N:
        break
ans = list(set(ans))
ans.sort()
for a in ans:
    print(a)
