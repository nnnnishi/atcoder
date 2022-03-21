S = input()
T = "oxx" * 10

for i in range(3):
    check = True
    for j in range(len(S)):
        if S[j] != T[i + j]:
            check = False
            break
    if check:
        print("Yes")
        exit()
print("No")

