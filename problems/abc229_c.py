import sys

input = sys.stdin.readline
N, W = list(map(int, input().split()))
ch = []
for i in range(N):
    A, B = [int(_) for _ in input().split()]
    ch.append([A, B])
ch.sort(reverse=True)

ans = 0
for i in range(N):
    if W > ch[i][1]:
        ans += ch[i][1] * ch[i][0]
        W -= ch[i][1]
    else:
        ans += W * ch[i][0]
        print(ans)
        exit()
print(ans)
