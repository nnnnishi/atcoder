N = int(input())
A = [int(_) for _ in input().split()]
cnt = 0
even_flg = False
for i in range(N):
    if A[i] % 2 != 0:
        cnt += 1
if cnt % 2 == 0:
    print("YES")
else:
    print("NO")
