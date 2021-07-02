# 再帰用
S = str(input())

cand = ["dream", "erase", "dreamer", "eraser"]
check = [0] * (len(S) + 1)
check[0] = 1
for i in range(len(S)):
    if check[i]:
        for s in cand:
            if i + len(s) <= len(S):
                if S[i : i + len(s)] == s:
                    check[i + len(s)] = 1

if check[len(S)]:
    print("YES")
else:
    print("NO")
