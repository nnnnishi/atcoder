N = int(input())
a = [int(_) for _ in input().split()]
a[0] -= 1
for i in range(N - 1):
    if a[i + 1] - a[i] < 0:
        exit(print("No"))
    else:
        if a[i + 1] - a[i] >= 1:
            a[i + 1] -= 1
print("Yes")
