N = 10
K = 5

# リストを用意
l = [0] * N
for i in range(N):
    # 入口で足す
    l[i] += 1
    if i + K < N:
        # 出口+1でひく
        l[i + K] -= 1
    else:
        break
print(l)
# 積む
for i in range(1, N):
    l[i] += l[i - 1]
print(l)