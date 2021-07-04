N, K = list(map(int, input().split()))
a = list(map(int, input().split()))
aorg = a[:]
a.sort()
dic = {}
for i in range(1, N + 1):
    dic[a[i - 1]] = i

# base
b = K // N
# amari
res = K % N

for ai in aorg:
    if dic[ai] <= res:
        print(b + 1)
    else:
        print(b)
