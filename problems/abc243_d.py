N, X = list(map(int, input().split()))
S = list(input().rstrip())
S2 = []
for s in S:
    if s == "U":
        if len(S2) > 0:
            pre = S2.pop()
            if pre == "R" or pre == "L":
                continue
            else:
                S2 += [pre, "U"]
        else:
            S2.append(s)
    else:
        S2.append(s)

for s in S2:
    if s == "U":
        if X % 2 == 0:
            X = X // 2
        else:
            X = (X - 1) // 2
    elif s == "R":
        X = X * 2 + 1
    elif s == "L":
        X = X * 2

print(X)
