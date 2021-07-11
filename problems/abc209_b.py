N, X = list(map(int, input().split()))
A = list(map(int, input().split()))
biki = N // 2
if (sum(A) - biki) <= X:
    print("Yes")
else:
    print("No")
