N = int(input())
a = [int(_) for _ in input().split()]

i = 0
cnt = 1
ans = []
check = set()
while cnt <= N:
    if a[i] == cnt:
        bi = i
        while cnt != i + 1:
            tmp = a[i - 1]
            a[i - 1] = a[i]
            a[i] = tmp
            ans.append(i)
            if i in check:
                exit(print(-1))
            check.add(i)
            i -= 1
        # print(i, bi - 1)
        i = cnt
        cnt += 1
    else:
        i += 1
if len(ans) == N - 1:
    for an in ans:
        print(an)
else:
    print(-1)
