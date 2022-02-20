S = input()
N = int(input())
a = [x for x in range(len(S))]

for _ in range(N):
    l, r = [int(_) for _ in input().split()]
    a[l - 1 : r] = list(reversed(a[l - 1 : r]))

for i in a:
    print(S[i], end="")
print()
