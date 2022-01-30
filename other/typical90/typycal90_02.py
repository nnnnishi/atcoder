N = int(input())
if N % 2 != 0:
    print()
    exit()


def dfs(ans, diff, pos):
    if pos == N:
        print(ans)
        return
    else:
        if diff + 1 <= N - pos - 1:
            dfs(ans + "(", diff + 1, pos + 1)
            ans = ans[:pos]
        if diff - 1 >= 0:
            dfs(ans + ")", diff - 1, pos + 1)
            ans = ans[:pos]
        return


dfs("", 0, 0)

