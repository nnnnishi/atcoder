X, Y = [int(_) for _ in input().split()]

# Xから
if X % 3 == 0:
    exit(print(0))
rX1 = X - (X // 3)
s1 = (X // 3) * Y
s2 = rX1 * (Y // 2)
if Y % 2 == 0:
    s3 = rX1 * (Y // 2)
else:
    s3 = rX1 * (Y // 2 + 1)
ans = max(s1, s2, s3) - min(s1, s2, s3)
# print("*", ans)
rX2 = X - (X // 3 + 1)
s1 = (X // 3 + 1) * Y
s2 = rX2 * (Y // 2)
if Y % 2 == 0:
    s3 = rX2 * (Y // 2)
else:
    s3 = rX2 * (Y // 2 + 1)
ans = min(max(s1, s2, s3) - min(s1, s2, s3), ans)
# print("**", ans)
# Yから
if Y % 3 == 0:
    exit(print(0))
rY1 = Y - (Y // 3)
s1 = (Y // 3) * X
s2 = rY1 * (X // 2)
if X % 2 == 0:
    s3 = rY1 * (X // 2)
else:
    s3 = rY1 * (X // 2 + 1)
ans = min(max(s1, s2, s3) - min(s1, s2, s3), ans)
# print("***", ans)
rY2 = Y - ((Y // 3) + 1)
s1 = ((Y // 3) + 1) * X
s2 = rY2 * (X // 2)
if X % 2 == 0:
    s3 = rY2 * (X // 2)
else:
    s3 = rY2 * ((X // 2) + 1)
ans = min(max(s1, s2, s3) - min(s1, s2, s3), ans)
# print("****", ans)

# 単純割
# Xから
ans = min(ans, Y * (X // 3 + 1) - Y * (X // 3))
ans = min(ans, X * (Y // 3 + 1) - X * (Y // 3))
print(ans)