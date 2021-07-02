A, B = list(map(int, input().split()))
if A == B:
    for i in range(A):
        if i != A - 1:
            print(i + 1, -1 * (i + 1), end=" ")
        else:
            print(i + 1, -1 * (i + 1))
else:
    if A > B:
        cnt = 0
        for i in range(A):
            if i < B - 1:
                print(i + 1, -1 * (i + 1), end=" ")
            if B - 1 <= i < A - 1:
                print(i + 1, end=" ")
                cnt += i + 1
            if i == A - 1:
                cnt += i + 1
                print(i + 1, -1 * cnt)
    else:
        cnt = 0
        for i in range(B):
            if i < A - 1:
                print(i + 1, -1 * (i + 1), end=" ")
            if A - 1 <= i < B - 1:
                print((i + 1) * -1, end=" ")
                cnt += i + 1
            if i == B - 1:
                cnt += i + 1
                print(cnt, (i + 1) * -1)
