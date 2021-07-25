import sys
from itertools import accumulate, product, permutations, combinations

sys.setrecursionlimit(1000000)


N = int(input())
K = int(input())
S = [list(input()) for i in range(N)]

ans = 0
visited = set()


# 深さ優先
def dfs(b, c):
    # すでにパターンを確認済みであれば探索しない
    if b in visited:
        return
    visited.add(b)
    # K個はいっていれば足す
    if c == K:
        global ans
        ans += 1
        return
    else:
        # 次行く場所を全探索
        for y, x in product(range(N), range(N)):
            # すでにえらんでいるか、#なら飛ばす
            if b >> (y * N + x) & 1 or S[y][x] == "#":
                continue
            # 次行く場所の周辺
            ok = False
            for y2, x2 in [[y, x + 1], [y, x - 1], [y + 1, x], [y - 1, x]]:
                # 道路の中、すでに入っている -> 連結になるのでそれをいれる
                if 0 <= x2 < N and 0 <= y2 < N and b >> (y2 * N + x2) & 1:
                    ok = True
                    break
            if ok:
                dfs((1 << (y * N + x) | b), c + 1)
        return


for sy in range(N):
    for sx in range(N):
        num = sy * N + sx
        if S[sy][sx] == ".":
            S[sy][sx] = "#"
            dfs(1 << num, 1)

print(ans)