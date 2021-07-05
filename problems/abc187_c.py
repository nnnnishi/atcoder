N = int(input())
s = set()
u = set()
for i in range(N):
    S = input()
    if S[0] == "!":
        u.add(S[1:])
    else:
        s.add(S)

for si in s:
    if si in u:
        exit(print(si))
print("satisfiable")
