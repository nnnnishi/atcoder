import numpy as np

N = int(input())
a = [int(_) for _ in input().split()]
b = list(np.array(a) + 1)
c = list(np.array(a) - 1)
d = a + b + c
d.sort()
count = 1
ans = 0
before = d[0]
for x in d[1:]:
    if before == x:
        count += 1
    else:
        ans = max(ans, count)
        count = 1
        before = x
ans = max(ans, count)
print(ans)