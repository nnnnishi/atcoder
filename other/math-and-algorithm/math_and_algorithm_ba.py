N = int(input())

s = set()
a = 1
s.add(a)
for i in range(1, 100):
    a *= 2
    s.add(a)
if N + 1 in s:
    print("Second")
else:
    print("First")

