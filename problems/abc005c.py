T = int(input())
N = int(input())
A = [int(_) for _ in input().split()]
M = int(input())
B = [int(_) for _ in input().split()]
idx = 0
for b in B:
    check = True
    while check:
        if idx == N:
            # 残りがないときはNo
            exit(print("no"))
        # idx個めのAがうれる
        if A[idx] <= b <= A[idx] + T:
            idx += 1
            check = False
        # うれなかったらつぎをみる
        else:
            idx += 1

print("yes")
