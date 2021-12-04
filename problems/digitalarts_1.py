S = input().split()
N = int(input())
F = []
for i in range(N):
    F.append(input())
ans = []
for s in S:
    is_f = False
    for f in F:
        if len(s) == len(f):
            cnt = 0
            for i in range(len(s)):
                if f[i] == "*" or f[i] == s[i]:
                    cnt += 1
            if cnt == len(s):
                is_f = True
    if is_f:
        ans.append("*" * len(s))
    else:
        ans.append(s)
print(*ans)
