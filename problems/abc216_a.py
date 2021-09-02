x, y = list(map(int, input().split(".")))

if 0 <= y <= 2:
    print(f"{x}" + "-")
elif 3 <= y <= 6:
    print(f"{x}")
else:
    print(f"{x}" + "+")
