# dfsで全列挙
def dfs(i, y):
    # yは数字の積
    if y + B > N:
        return
    # Nを超えていなければ追加
    yy.append(y)
    # 積は素数だけ考えればOK
    for j in range(i, 4):
        # 2,3,5,7の順で数えれば網羅される
        dfs(j, y * primes[j])


def f(x):
    res = 1
    while x:
        # 桁ごとに足す
        x, r = divmod(x, 10)
        res *= r
    return res


yy = [0]
primes = [2, 3, 5, 7]

N, B = map(int, input().split())

if N < B:
    print(0)
    exit()

dfs(0, 1)

ans = 0
# yyはすべてのパターン
for y in yy:
    if f(y + B) == y:
        ans += 1

print(ans)
