N = int(input())
s = set()
for i in range(N):
    S = input()
    if S in s:
        exit(print("Yes"))
    else:
        s.add(S)
print("No")
