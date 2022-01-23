a, b, c = [int(_) for _ in input().split()]


L = [a % 10]
ok = True
idx = 0
orga = a
for i in range(1, 11):
    a *= orga
    a %= 10
    if a not in L:
        L.append(a)
    else:
        break
# print(L)
idx = pow(b, c, len(L))
# print(idx)
print(L[(idx - 1) % len(L)])
