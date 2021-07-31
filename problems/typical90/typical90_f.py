# import numpy as np

n, k = map(int, input().split())
s = list(input())
ls = len(s) + 1
nex = [[0] * ls for _ in range(26)]

# 前計算
for i in range(26):
    nex[i][len(s)] = len(s)
# 文字数の逆から
for i in range(len(s))[::-1]:
    for j in range(26):
        if (ord(s[i]) - ord("a")) == j:
            nex[j][i] = i
        else:
            nex[j][i] = nex[j][i + 1]
# DP
# print(np.array(nex))

# 貪欲法
ans = []
current_pos = 0
for i in range(1, k + 1):
    for j in range(26):
        # なんばんめに文字jが次出てくるか
        next_pos = nex[j][current_pos]
        # 文字jが次出てきたところから最大で何文字あるか
        max_ps_length = int(len(s) - next_pos - 1) + i
        # k文字以上あればその文字は追加する
        if k <= max_ps_length:
            ans.append(chr(ord("a") + j))
            # 追加した文字のところまでposをずらす
            current_pos = next_pos + 1
            break

print("".join(ans))