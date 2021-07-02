N, M = list(map(int, input().split()))
graph = []
for i in range(N):
    graph.append([])
for i in range(M):
    Ai, Bi = list(map(int, input().split()))
    graph[Ai - 1].append(Bi - 1)
    graph[Bi - 1].append(Ai - 1)

color = [-1] * N
done = [False] * N
color[0] = 0
ans = 1


def dfs(i, cnt):
    global done
    global color
    done[i] = True
    print(i, cnt, done, color)
    for c in range(3):
        # print("c", "*", c)
        ok = True
        for x in graph[i]:
            if color[x] != c:
                continue
            else:
                ok = False
                break
        if ok:
            cnt += 1
            color[i] = c
            for x in graph[i]:
                if not done[x]:
                    cnt += dfs(x, cnt)
                    color[i] = -1
                    done[i] = False
    return cnt


for i in range(0, N):
    if not done[i]:
        print("ans", done)
        ans *= dfs(i, 0)

print(ans)