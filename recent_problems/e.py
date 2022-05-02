from collections import deque


N, K = list(map(int, input().split()))
S = input()
b = S[0]
init = b
cnt = 1
q = deque()
for i in range(1, len(S)):
    if b == S[i]:
        cnt += 1
    else:
        q.append((int(b), cnt))
        b = S[i]
        cnt = 1
q.append((int(b), cnt))

knum = 0
ans = 0
cnt = 0
q2 = deque()
while len(q) > 0:
    n, c = q.popleft()
    if n == 0:
        if knum < K:
            q2.append((n, c))
            cnt += c
            ans = max(cnt, ans)
            knum += 1
        else:
            n2, c2 = q2.popleft()
            cnt -= c2
            if n2 == 0:
                q2.append((n, c))
                cnt += c
                ans = max(cnt, ans)
            else:
                n2, c2 = q2.popleft()
                cnt -= c2
                if n2 == 0:
                    q2.append((n, c))
                    cnt += c
                    ans = max(cnt, ans)
    else:
        q2.append((n, c))
        cnt += c
        ans = max(cnt, ans)
print(ans)
