N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
cnt = 0
for i in range(N):
    if A[i] == B[i]:
        cnt += 1
print(cnt)
cnt = 0
for i in range(N):
    for j in range(N):
        if i != j and A[i] == B[j]:
            cnt += 1
print(cnt)
