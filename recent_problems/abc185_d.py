N, M = [int(_) for _ in input().split()]
A = [int(_) for _ in input().split()]
if M == 0:
    print(1)
    exit()
A.sort()
b = 0
span = []
for a in A:
    l = a - b - 1
    b = a
    if l >= 1:
        span.append(l)

if N - b >= 1:
    span.append(N - b)
# print(span)
if len(span) == 0:
    print(0)
else:
    c = min(span)
    ans = 0
    for d in span:
        ans += -(-d // c)
    print(ans)

