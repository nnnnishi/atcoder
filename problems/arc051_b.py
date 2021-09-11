N = int(input())

a = 2
b = 1
while N != 1:
    tmp = a
    a = tmp + b
    b = tmp
    N -= 1
print(a, b)
