s, t = list(input().split())
a, b = list(map(int, input().split()))
u = input()
if u == s:
    print(a - 1, b)
else:
    print(a, b - 1)
