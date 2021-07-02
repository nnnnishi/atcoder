N = int(input())
A = [int(_) for _ in input().split()]

maxA = max(A)
check = [False] + [False] * maxA
setA = set()
outA = set()
for a in A:
    if a in setA:
        outA.add(a)
    else:
        check[a] = True
        setA.add(a)

for n in range(1, maxA + 1):
    if check[n]:
        c = n + n
        while c <= maxA:
            check[c] = False
            c += n

# Trueの数を数える
print(sum([1 for i in range(len(check)) if check[i] and i not in outA]))
