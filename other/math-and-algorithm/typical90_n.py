N = int(input())
A = [int(_) for _ in input().split()]
B = [int(_) for _ in input().split()]
A.sort()
B.sort()
ans = 0
for a, b in zip(A, B):
    ans += abs(a - b)
print(ans)
