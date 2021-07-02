N = int(input())
A = [int(_) for _ in input().split()]
mod = (10 ** 9) + 7
sumA = 0
for i in range(N):
    sumA += A[i] % mod

ans = 0
for i in range(N - 1):
    sumA = ((sumA % mod) - (A[i] % mod)) % mod
    ans += ((A[i] % mod) * (sumA % mod)) % mod
    ans = ans % mod
print(ans)