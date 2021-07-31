N = int(input())
A = [int(_) for _ in input().split()]
sumA = [0]
tot = 0
for i in range(2 * N):
    j = i % N
    sumA.append(sumA[i] + A[j])
    if i < N:
        tot += A[i]
if tot % 10 != 0:
    exit(print("No"))
c = tot // 10
j = 1
for i in range(2 * N + 1):
    while j <= 2 * N and sumA[j] - sumA[i] < c:
        j += 1
    if j <= 2 * N and sumA[j] - sumA[i] == c:
        exit(print("Yes"))
    else:
        continue
print("No")
