N = int(input())
S = list(input())

for i in range(len(S)):
    s = ord(S[i]) + N
    if s > 90:
        s -= 26
    S[i] = chr(s)
print("".join(S))

