A, B = list(map(int, input().split()))
if B < A:
    print("No")
elif B > 6 * A:
    print("No")
else:
    print("Yes")
