# 区間でのエラトステネスの篩

L, R = [int(_) for _ in input().split()]
N = R - L + 1
# 0はじまり、Nまで (L,L+1,...,R)
is_prime = [1] * N
if L == 1:
    is_prime[0] = 0
for n in range(2, R):
    # root R までみれば十分
    if n ** 2 > R:
        break
    if n >= L:
        if is_prime[n - L]:
            check = n + n
            while check <= R:
                is_prime[check - L] = 0
                check += n
    else:
        # 最初は -(-L//n) * n
        check = -(-L // n) * n
        while check <= R:
            is_prime[check - L] = 0
            check += n

print(sum(is_prime))
