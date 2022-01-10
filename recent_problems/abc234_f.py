from collections import Counter, deque, defaultdict

S = input()
ls = len(S)
d = Counter(list(S))
for n in range(1,ls+1):
    for j in range(1,n+1):
N = list(map(int, input().split()))
