import sys
from operator import itemgetter

input = sys.stdin.readline

N, K = [int(_) for _ in input().split()]
d = []
for _ in range(N):
    d.append([int(_) for _ in input().split()])
d.sort(key=itemgetter(0))
ans = 10 ** 30
for i1 in range(N):
    for i2 in range(i1 + K - 1, N):
        for j1 in range(N):
            for j2 in range(j1 + 1, N):
                if d[j1][1] < d[j2][1]:
                    cnt = 0
                    for x in range(N):
                        if (
                            d[i1][0] <= d[x][0] <= d[i2][0]
                            and d[j1][1] <= d[x][1] <= d[j2][1]
                        ):
                            cnt += 1

                    if cnt >= K and (d[j2][1] - d[j1][1]) * (d[i2][0] - d[i1][0]) < ans:
                        ans = (d[j2][1] - d[j1][1]) * (d[i2][0] - d[i1][0])
                else:
                    cnt = 0
                    for x in range(N):
                        if (
                            d[i1][0] <= d[x][0] <= d[i2][0]
                            and d[j2][1] <= d[x][1] <= d[j1][1]
                        ):
                            cnt += 1

                    if cnt >= K and (d[j1][1] - d[j2][1]) * (d[i2][0] - d[i1][0]) < ans:
                        ans = (d[j1][1] - d[j2][1]) * (d[i2][0] - d[i1][0])


print(ans)
