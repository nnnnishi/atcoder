N = int(input())
cnt = 0
while N > 0:
    if cnt % 2 == 0:
        N = N // 2
    else:
        N = (N - 1) // 2
    cnt += 1
if cnt % 2 != 0:
    print("Aoki")
else:
    print("Takahashi")
