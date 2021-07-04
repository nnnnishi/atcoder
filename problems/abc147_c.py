N = int(input())
A = [[] for i in range(N)]
for i in range(N):
    a = int(input())
    for j in range(a):
        x, y = [int(_) for _ in input().split()]
        A[i].append([x - 1, y])


def has_bit(n, i):
    return (n & 1 << i) > 0


# N桁の0-1の組合せパターン数 1<<N
ans = 0
for n in range(1 << N):
    cnt = 0
    ok = True
    # N桁
    for i in range(N):
        # パターンnのi桁目が1 -> 正直
        if has_bit(n, i):
            cnt += 1
            # 正直者の証言をチェック
            for xi, yi in A[i]:
                # print(n, xi, "c")
                if has_bit(n, xi) != yi:
                    # print(n, "*")
                    ok = False

    if ok == True:
        # print(n, cnt, "*")
        ans = max(ans, cnt)
print(ans)