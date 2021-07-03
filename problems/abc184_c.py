a, b = [int(_) for _ in input().split()]
c, d = [int(_) for _ in input().split()]
c = c - a
d = d - b

if c == d == 0:
    exit(print(0))
# 1手
if c == d or c == -d or abs(c) + abs(d) <= 3:
    exit(print(1))
# 2手
if (
    (c - 4 <= d <= c + 4)
    or (-c - 4 <= d <= -c + 4)
    or (c + d) % 2 == 0
    or (d == 0 and abs(c) <= 6)
    or (c == 0 and abs(d) <= 6)
):
    print(2)
else:
    print(3)
