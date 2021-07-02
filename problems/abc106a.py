S = input()
K = int(input())

cnt = 0
last = 0
for i in range(len(S)):
    if S[i] == "1":
        cnt += 1
    else:
        last = int(S[i])
        break
if K <= cnt:
    print(1)
else:
    print(last)