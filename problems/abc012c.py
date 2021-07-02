N = int(input())
a = 0
for i in range(1, 10):
    for j in range(1, 10):
        a += i * j
c = a - N
for i in range(1, 10):
    for j in range(1, 10):
        if c == i * j:
            print(f"{i} x {j}")
