S = input()

b = S[0]
cnt = 0
ans = ""
for s in S:
    if s != b:
        ans += b + str(cnt)
        b = s
        cnt = 1
    else:
        cnt += 1

ans += b + str(cnt)
print(ans)
