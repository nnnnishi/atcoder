N = int(input())
a = [int(_) for _ in input().split()]
a.sort()
t = N // 2 - 1
print(a[t + 1] - a[t])
