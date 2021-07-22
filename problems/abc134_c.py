N = int(input())
a = []
max_cnt = 0
max_x = 0
nx_max = 0
for i in range(N):
    x = int(input())
    a.append(x)
    if x > max_x:
        nx_max = max_x
        max_x = x
        max_cnt = 1
    elif x == max_x:
        nx_max = max_x
        max_cnt += 1
    elif x >= nx_max:
        nx_max = x
# print(max_x, max_cnt, nx_max)

for xi in a:
    if xi != max_x:
        print(max_x)
    elif xi == max_x:
        if max_cnt >= 2:
            print(max_x)
        else:
            print(nx_max)