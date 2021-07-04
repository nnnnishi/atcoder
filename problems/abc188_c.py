N = int(input())
l = 2 ** N
A = [int(_) for _ in input().split()]
# さいだいのやつ
top_i = 0
top_r = 0
for i in range(l):
    if A[i] > top_r:
        top_i = i
        top_r = A[i]

if top_i >= l // 2:
    top_i = 0
    top_r = 0
    for i in range(l // 2):
        if A[i] > top_r:
            top_i = i
            top_r = A[i]
else:
    top_i = 0
    top_r = 0
    for i in range(l // 2, l):
        if A[i] > top_r:
            top_i = i
            top_r = A[i]
print(top_i + 1)
