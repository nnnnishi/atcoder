A, B = input().rstrip().split(" ")
for i in range(min(len(A), len(B))):
    if int(A[len(A) - 1 - i]) + int(B[len(B) - 1 - i]) > 9:
        print("Hard")
        exit()
print("Easy")

