from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

dic = {}

N = int(input())
P = list(map(int, input().split()))
Q = int(input())
q = []
for i in range(Q):
    U, D = list(map(int, input().split()))
    q.append([U, D])

# おやまでたどる
for i in range(N - 1):
    n_i = i
    l = 0
    nodes = []
    node = -1
    while node != 1:
        l += 1
        node = int(P[n_i])
        nodes.append(node)
        n_i = node - 
    for n in nodes:
        dic.setdefault(n, {})
        dic[n].setdefault(l, 0)
        dic[n][l] += 1
for query in q:
    print(dic[query[0]][query[1]])
