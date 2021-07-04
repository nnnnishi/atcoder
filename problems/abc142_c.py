N = int(input())
a = [int(_) for _ in input().split()]
dic = {}
for i in range(N):
    dic[a[i] - 1] = i
print(*[dic[i] + 1 for i in range(N)])
