H, N = list(map(int, input().split()))
A = [int(_) for _ in input().split()]
A.sort(reverse=True)
if sum(A) >= H:
    print("Yes")
else:
    print("No")
