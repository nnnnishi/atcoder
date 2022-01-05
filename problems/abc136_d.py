S = list(input())
A = [0] * len(S)
pos = 0
cum = 0
pre = "R"
for i in range(len(S)):
    if pre == "R" and S[i] == "R":
        cum += 1
    elif pre == "L" and S[i] == "L":
        cum += 1
    elif pre == "R" and S[i] == "L":
        pos = i
        A[pos - 1] += cum // 2 + cum % 2
        A[pos] += cum // 2
        pre = "L"
        pos = i - 1
        cum = 1
    elif pre == "L" and S[i] == "R":
        A[pos + 1] += cum // 2 + cum % 2
        A[pos] += cum // 2
        pre = "R"
        cum = 1
A[pos + 1] += cum // 2 + cum % 2
A[pos] += cum // 2
print(*A)
