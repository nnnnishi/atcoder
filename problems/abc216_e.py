N, K = list(map(int, input().split()))
A = [int(_) for _ in input().split()] + [0]

A.sort(reverse=True)
k = 0
ans = 0
for i in range(N):
    if A[i] != A[i + 1]:
        # かず、項数、
        cnt = (i + 1) * (A[i] - A[i + 1])
        sat = (i + 1) * (A[i] + (A[i + 1] + 1)) * (A[i] - A[i + 1]) // 2
        if k + cnt <= K:
            ans += sat
            k += cnt
            # print(cnt)
            # print(ans)
        else:
            ret = (K - k) // (i + 1)
            res = (K - k) % (i + 1)
            # print(ret, res)
            # for j in range(ret):
            #    ans += (A[i] - j) * (i + 1)
            ans += (i + 1) * (A[i] + (A[i] - ret + 1)) * ret // 2
            ans += (A[i] - ret) * res
            exit(print(ans))
print(ans)