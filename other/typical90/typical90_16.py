N = int(input())
A = [int(_) for _ in input().split()]
A.sort(reverse=True)
ans = 10 ** 5
for i in range(10 ** 5):
    if A[0] * i > N:
        break
    elif A[0] * i == N:
        if ans > i:
            ans = i
    for j in range((10 ** 5) - i):
        if A[0] * i + A[1] * j > N:
            break
        elif A[0] * i + A[1] * j == N:
            if ans > i + j:
                ans = i + j
        elif (N - (A[0] * i + A[1] * j)) % A[2] == 0:
            if ans > i + j + (N - (A[0] * i + A[1] * j)) // A[2]:
                ans = i + j + (N - (A[0] * i + A[1] * j)) // A[2]

print(ans)
