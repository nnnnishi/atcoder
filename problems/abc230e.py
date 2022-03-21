import math
N = int(input())
ans = 0
cand = []
M = int(math.sqrt(N)//1)
for i in range(1, M+1):
    ans += N // i
ans *=2
ans -= M**2
print(ans)
