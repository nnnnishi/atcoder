a, b = list(map(int, input().split()))
X = int(str(a) + str(b))
for i in range(1000):
    if i ** 2 == X:
        exit(print("Yes"))
print("No")