a = [int(_) for _ in input().split()]
a.sort()
if a[0] + a[1] == a[2]:
    print("Yes")
else:
    print("No")

