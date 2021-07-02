a, b, w = list(map(int, input().split()))
w = w * 1000
mi = 10 ** 10
ma = -1
d = b - a
# max
for i in range((w // a) + 1):
    if (w - (i * a)) <= d * i:
        tmp = i
        ma = max(tmp, ma)
# min
for i in range((w // b) + 2):
    if ((i * b) - w) >= 0 and ((i * b) - w) <= d * i:
        tmp = i
        mi = min(tmp, mi)
if ma == -1:
    print("UNSATISFIABLE")
else:
    print(mi, ma)
