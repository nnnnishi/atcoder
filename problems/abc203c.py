N, K = list(map(int, input().split()))
pair = []
for i in range(N):
    pair.append(list(map(int, input().split())))
pair.sort()

for i in range(N):
    A = pair[i][0]
    B = pair[i][1]
    if A <= K:
        K += B
    else:
        exit(print(K))
print(K)