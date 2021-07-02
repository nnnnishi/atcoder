A, B = list(input().split())
print(
    max(
        int("9" + A[1] + A[2]) - int(B),
        int(A[0] + "9" + A[2]) - int(B),
        int(A[0] + A[1] + "9") - int(B),
        int(A) - int("1" + B[1] + B[2]),
        int(A) - int(B[0] + "0" + B[2]),
        int(A) - int(B[0] + B[1] + "0"),
    )
)
