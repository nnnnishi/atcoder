N = int(input())
a = [int(_) for _ in input().split()]
s = set()
count = 0
for ai in a:
    if 1 <= ai <= 399:
        s.add("1")
    elif 400 <= ai <= 799:
        s.add("2")
    elif 800 <= ai <= 1199:
        s.add("3")
    elif 1200 <= ai <= 1599:
        s.add("4")
    elif 1600 <= ai <= 1999:
        s.add("5")
    elif 2000 <= ai <= 2399:
        s.add("6")
    elif 2400 <= ai <= 2799:
        s.add("7")
    elif 2800 <= ai <= 3199:
        s.add("8")
    else:
        count += 1

if len(s) > 0:
    print(len(s), len(s) + count)
else:
    print(1, count)