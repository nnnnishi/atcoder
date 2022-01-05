N = int(input())
d = {}
for i in range(N):
    d[i + 1] = int(input())
x = 1
exist = set()
exist.add(1)
x = d[1]
ans = 1
while x != 2:
    if x in exist:
        print(-1)
        exit()
    else:
        exist.add(x)
        ans += 1
        x = d[x]
print(ans)
