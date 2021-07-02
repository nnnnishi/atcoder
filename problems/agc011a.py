N, C, K = [int(_) for _ in input().split()]
T = [int(input()) for i in range(N)]
# print(N, C, K)
T.sort()
ans = 1
S = T[0] + K
ride = 1
for i in range(1, N):
    # print("**", T[i], S, ride, C)
    if ride >= C:
        ans += 1
        S = T[i] + K
        ride = 1
        # print("*A", T[i], S, ride, C)
    else:
        if T[i] <= S:
            ride += 1
            # print("*B", T[i], S, ride, C)
        else:
            # print("*", i)
            ans += 1
            S = T[i] + K
            ride = 1
            # print("*C", T[i], S, ride, C)
print(ans)
