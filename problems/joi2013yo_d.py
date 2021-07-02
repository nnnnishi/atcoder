D, N = [int(_) for _ in input().split()]
T = []
for _ in range(D):
    T.append(int(input()))
A = []
B = []
C = []
for _ in range(N):
    a, b, c = [int(_) for _ in input().split()]
    A.append(a)
    B.append(b)
    C.append(c)

score = []
for d in range(D):
    score.append([-1] * 101)

# 1日目
for j in range(len(A)):
    if A[j] <= T[0] <= B[j]:
        score[0][C[j]] = 0

for idx in range(1, D):
    for j in range(len(A)):
        # きれる
        if A[j] <= T[idx] <= B[j]:
            for k in range(101):
                if score[idx - 1][k] >= 0:
                    score[idx][C[j]] = max(
                        score[idx][C[j]], abs(k - C[j]) + score[idx - 1][k]
                    )
print(max(score[D - 1]))
