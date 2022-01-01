T = int(input())
for i in range(T):
    c = int(input())
    if c % 4 == 0:
        print("Even")
    elif c % 2 == 0:
        print("Same")
    else:
        print("Odd")

