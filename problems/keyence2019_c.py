N = int(input())
a = [int(_) for _ in input().split()]
b = [int(_) for _ in input().split()]
q = []
for ai, bi in zip(a, b):
    q.append([bi - ai, ai, bi])
q.sort(reverse=True)

ans = 0
cum = 0

for x, ai, bi in q:
    if x > 0:
        ans += 1
        cum += x
    else:
        break
q.sort()
if cum == 0:
    exit(print(0))

for x, ai, bi in q:
    if cum <= 0:
        exit(print(ans))
    if x < 0:
        ans += 1
        cum += x

print(-1)
