N = int(input())
S = list(input())
b = S[0]
cnt = 1
q = []
for i in range(1, N):
    if b == S[i]:
        cnt += 1
        continue
    else:
        q.append([b, cnt])
        cnt = 1
        b = S[i]
q.append([b, cnt])

ans = 0
while len(q) > 1:
    b, cnt = q.pop()
    N -= cnt
    ans += cnt * N
print(ans)
