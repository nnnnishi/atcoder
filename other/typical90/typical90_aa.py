N = int(input())
c = set()
for i in range(N):
    S = input()
    if S in c:
        continue
    else:
        c.add(S)
        print(i + 1)
