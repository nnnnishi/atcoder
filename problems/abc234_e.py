from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort

N = int(input())

L = [x for x in range(1, 10)]
for i in range(1, 10):
    for d in range(-9, 10):
        px = i
        x = i
        while 0 <= px + d <= 9 and int(str(x) + str(px + d)) <= 10 ** 19:
            x = int(str(x) + str(px + d))
            px += d
            L.append(x)
L.sort()
print(L[bisect_left(L, N)])

