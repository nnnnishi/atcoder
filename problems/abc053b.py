S = input()
startA = -1
endZ = -1
for i in range(len(S)):
    if S[i] == "A":
        if startA == -1:
            startA = i
    if S[i] == "Z":
        endZ = i
print(endZ - startA + 1)
