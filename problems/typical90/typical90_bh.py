import bisect

N = int(input())
a = [int(_) for _ in input().split()]

# 最大値+1,空で生成すると10**6の初期化リストができる
right = [0] * (N)
left = [0] * (N)
right[0] = 1
# みぎがわにふやす
LIS = [a[0]]
for i in range(1, N):
    if a[i] > LIS[-1]:
        LIS.append(a[i])
    else:
        LIS[bisect.bisect_left(LIS, a[i])] = a[i]
    right[i] = len(LIS)

left[N - 1] = 1
# 左側にふやす
LIS = [a[N - 1]]
for i in range(N - 2, -1, -1):
    if a[i] > LIS[-1]:
        LIS.append(a[i])
    else:
        LIS[bisect.bisect_left(LIS, a[i])] = a[i]
    left[i] = len(LIS)

ans = 0
for i in range(N):
    ans = max(left[i] + right[i] - 1, ans)
print(ans)