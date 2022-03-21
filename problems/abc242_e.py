import sys

input = sys.stdin.readline
M = 998244353
T = int(input())
for _ in range(T):
    N = int(input())
    S = list(input().rstrip())
    mid = -(-N // 2)
    cnt = ord(S[mid - 1]) - 65 + 1
    if N % 2 == 0:
        newS = S[:mid] + S[:mid][::-1]
        check = [S, newS]
        check.sort()
        if not (S == newS or check[0] == newS):
            cnt -= 1
    else:
        newS = S[:mid] + S[: mid - 1][::-1]
        check = [S, newS]
        check.sort()
        if not (S == newS or check[0] == newS):
            cnt -= 1
    for i in range(mid - 2, -1, -1):
        cnt += (ord(S[i]) - 65) * pow(26, (mid - 2) + 1 - i, M)
        cnt %= M
    print(cnt)

