N = int(input())
l = []
for i in range(5):
    l.append(int(input()))
minl = min(l)

print(4 + (-(-N // minl)))
