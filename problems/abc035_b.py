S = list(input())
A = int(input())
x = 0
y = 0
c = 0
for i in range(len(S)):
    if S[i] == "U":
        y += 1
    elif S[i] == "D":
        y -= 1
    elif S[i] == "L":
        x -= 1
    elif S[i] == "R":
        x += 1
    elif S[i] == "?":
        c += 1

if A == 1:
    print(abs(x) + abs(y) + c)
else:
    if c <= abs(x) + abs(y):
        print(abs(x) + abs(y) - c)
    else:
        if (c - abs(x) + abs(y)) % 2 == 0:
            print(0)
        else:
            print(1)
