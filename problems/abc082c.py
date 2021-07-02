from collections import Counter

N = int(input())
a = list(map(int, input().split()))

c = Counter(a)
ans = 0
for k, v in c.items():
    if k != v:
        if k > v:
            ans += v
        else:
            ans += v - k
print(ans)
