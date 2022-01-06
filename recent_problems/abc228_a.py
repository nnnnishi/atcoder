a, b, c = list(map(int, input().split()))
if a > b:
    b += 24
if a > c:
    c += 24
if a <= c < b:
    print("Yes")
else:
    print("No")

