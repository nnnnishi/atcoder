from collections import defaultdict

N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

dic = defaultdict(int)
for a in A:
    dic[a] += 1
count = []
for i in dic:
    count.append(dic[i])
n = len(count)
if n < K:
    print(0)
else:
    ans = 0
    n1 = n - K
    count.sort()
    print(sum(count[:n1]))
