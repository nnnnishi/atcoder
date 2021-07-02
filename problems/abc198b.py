N = int(input())
tmpn = N
for i in range(11):
    if tmpn % 10 == 0:
        tmpn = tmpn // 10
    else:
        break
d = len(list(str(tmpn)))
ok = True
for i in range(d // 2 + 1):
    if str(tmpn)[i] != str(tmpn)[d - 1 - i]:
        ok = False
        break
if ok:
    print("Yes")
else:
    print("No")