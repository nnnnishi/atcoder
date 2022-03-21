from operator import itemgetter

N, D = list(map(int, input().split()))
w = []
for _ in range(N):
    w.append(list(map(int, input().split())))
w.sort(key=itemgetter(1, 0))

ans = 0
idx = 0
while idx < N:
    ans += 1
    right = w[idx][1]
    idx += 1
    while idx < N:
        if w[idx][0] <= right + D - 1:
            idx += 1
        else:
            break
print(ans)
