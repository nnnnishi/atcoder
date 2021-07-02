N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
mB = min(B)
mA = max(A)
if mB - mA + 1 <= 0:
    print(0)
else:
    print(mB - mA + 1)
