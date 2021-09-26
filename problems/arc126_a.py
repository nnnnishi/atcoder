T = int(input())
query = []
for i in range(T):
    query.append([int(_) for _ in input().split()])

for n2, n3, n4 in query:
    ans = 0
    # print(n2, n3, n4)
    # 3*2と4からつくる
    if n3 >= n4 * 2:
        ans += n4
        n3 -= n4 * 2
        n4 = 0
    else:
        ans += n3 // 2
        n4 -= n3 // 2
        n3 -= (n3 // 2) * 2

    # print(n2, n3, n4, ans)
    # 3と2からつくる
    if n3 >= n2:
        ans += n2 // 2
        n2 -= (n2 // 2) * 2
        n3 -= (n2 // 2) * 2
    else:
        ans += n3 // 2
        n2 -= (n3 // 2) * 2
        n3 -= (n3 // 2) * 2
    # print(n2, n3, n4, ans)
    # 4*2と2*1からつくる
    if n4 >= n2 * 2:
        ans += n2
        n4 -= n2 * 2
        n2 -= n2
    else:
        ans += n4 // 2
        n2 -= n4 // 2
        n4 -= (n4 // 2) * 2
    # print(n2, n3, n4, ans)
    # 2*3と4からつくる
    if n2 >= n4 * 3:
        ans += n4
        n2 -= n4 * 3
        n4 = 0
    else:
        ans += n2 // 3
        n4 -= n2 // 3
        n2 -= (n2 // 3) * 3

    ans += n2 // 5
    # print(n2, n3, n4, ans)
    print(ans)

