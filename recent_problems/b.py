l, h = list(map(int, input().split()))
N = int(input())
for _ in range(N):
    t = int(input())
    if t <= l:
        print(l - t)
    elif t > h:
        print(-1)
    else:
        print(0)
