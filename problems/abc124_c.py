S = list(map(int, input()))

s = 0
t1 = 0
for i in range(len(S)):

    if S[i] != s:
        t1 += 1
    s += 1
    s = s % 2

s = 1
t2 = 0
for i in range(len(S)):

    if S[i] != s:
        t2 += 1
    s += 1
    s = s % 2

print(min(t1, t2))
