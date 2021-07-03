N = int(input())
a = []
for i in range(N):
    a.append(int(input()))
alist = list(set(a))
alist.sort()
d = {}
for i in range(len(alist)):
    d[alist[i]] = i
for ai in a:
    print(d[ai])
