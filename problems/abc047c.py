S = list(input())
ans = -1
left = 0
right = len(S) - 1

# 左から
while right - left > -1:
    # 左
    left_cnt = 1
    for tmp in range(left, right):
        if S[tmp] == S[tmp + 1]:
            left_cnt += 1
        else:
            break
    # 右
    right_cnt = 1
    for tmp in range(right, left, -1):
        if S[tmp] == S[tmp - 1]:
            right_cnt += 1
        else:
            break
    # print(left_cnt, right_cnt)
    if left_cnt >= right_cnt:
        left += left_cnt
    #    print("L")
    else:
        right -= right_cnt
    #    print("R")
    ans += 1
    # print(left, right)
print(ans)
