l = ["ABC", "ARC", "AGC", "AHC"]
d = {}
for li in l:
    d[li] = 0
for i in range(3):
    S = input()
    d[S] += 1
for li in l:
    if d[li] == 0:
        print(li)
