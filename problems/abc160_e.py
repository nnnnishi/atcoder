X, Y, A, B, C = [int(_) for _ in input().split()]
x = [int(_) for _ in input().split()]
y = [int(_) for _ in input().split()]
z = [int(_) for _ in input().split()]
x.sort(reverse=True)
y.sort(reverse=True)
all = x[:X] + y[:Y] + z
all.sort(reverse=True)
print(sum(all[: (X + Y)]))
