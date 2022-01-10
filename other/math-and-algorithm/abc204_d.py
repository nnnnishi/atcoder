N = int(input())
T = [int(_) for _ in input().split()]
T.sort(reverse=True)
a = 0
b = 0

for t in T:
    if a > b:
        b += t
    else:
        a += t
print(max(a, b))
