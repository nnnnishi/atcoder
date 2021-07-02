import sys

sys.setrecursionlimit(1000000)

N = int(input())
C = list(map(int, input().split()))
graph = []
for i in range(N):
    graph.append([])

for _ in range(N - 1):
    A, B = list(map(int, input().split()))
    graph[A - 1].append(B - 1)
    graph[B - 1].append(A - 1)

C_list = [0] * (10 ** 5 + 1)
ok_n = []


def dfs(i, p):
    global C_list
    # デフォルト値
    if C_list[C[i]] == 0:
        ok_n.append(i + 1)
    C_list[C[i]] += 1
    for j in graph[i]:
        if j != p:
            dfs(j, i)
    C_list[C[i]] -= 1


dfs(0, 0)
ok_n.sort()
for i in range(len(ok_n)):
    print(ok_n[i])