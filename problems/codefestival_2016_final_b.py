N = int(input())
cnt = 0
ans = []
if N == 1:
    exit(print(1))
if N == 2:
    exit(print(2))
for i in range(1, N):
    cnt += i
    ans.append(i)
    if cnt > N:
        break
ex = cnt - N
for a in ans:
    if a != ex:
        print(a)
