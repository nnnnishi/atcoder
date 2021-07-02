S = input()
A = "WBWBWWBWBWBW" * 10
i = 0
dic = {0: "Do", 2: "Re", 4: "Mi", 5: "Fa", 7: "So", 9: "La", 11: "Si"}
for i in range(20):
    if S == A[i + 0 : i + 20]:
        exit(print(dic[i]))
