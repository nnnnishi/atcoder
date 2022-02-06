S = list(input())
T = list(input())
no = "UNRESTORABLE"
if len(T) > len(S):
    print(no)
    exit()

for s in range(len(S) - len(T), -1, -1):
    for t in range(len(T)):
        ok = True
        if S[s + t] == "?" or S[s + t] == T[t]:
            continue
        else:
            ok = False
            break
    if ok:
        for t in range(len(T)):
            S[s + t] = T[t]
        print("".join(S).replace("?", "a"))
        exit()
print(no)
