N = int(input())
A = [int(_) for _ in input().split()]
sumA = sum(A)
lenA = len(A)
ans = 0
for a in A:
    ans += (lenA - 1) * (a ** 2)
    sumA -= a
    ans -= 2 * a * sumA
print(ans)
