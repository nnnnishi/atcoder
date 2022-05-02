# https://atcoder.jp/contests/typical90/tasks/typical90_cj
# 鳩の巣原理
# 和が N になるパターンは N+1 探索すれば必ずダブる
# dfsで入れる場合、入れない場合を探索

N, Q = map(int, input().split())
A = list(map(int, input().split()))

ban = [[] for _ in range(N + 1)]
for _ in range(Q):
    X, Y = map(int, input().split())
    ban[Y - 1].append(X - 1)

ans = [None] * 8889

selected = [False] * (N)


def output(B, C):
    # B,Cはそれぞれ選択したもの
    x = sum(B)
    y = sum(C)
    print(x)
    print(*(i + 1 for i in range(N) if B[i]))
    print(y)
    print(*(i + 1 for i in range(N) if C[i]))
    exit()


# dfsで全列挙
def dfs(i, s):
    if i == N:
        if ans[s]:
            output(ans[s], selected)
        else:
            ans[s] = selected[:]
        return
    else:
        # いれる、いれない
        # print("*", i, a, s)
        dfs(i + 1, s)
        for j in ban[i]:
            if selected[j]:
                break
        else:
            selected[i] = True
            dfs(i + 1, s + A[i])
            selected[i] = False


dfs(0, 0)
