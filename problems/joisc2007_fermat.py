from collections import Counter, deque, defaultdict

p = int(input())
n = int(input())

powd = {}
powd[0] = 0
powd[1] = 1
powc = defaultdict(int)
powc[0] = 1
powc[1] = 1
for i in range(2, p):
    powd[i] = pow(i, n, p)
    powc[powd[i]] += 1


l = len(powc)
ans = 0
print(powc)
for i in range(p):
    # https://manabitimes.jp/math/576
    # i**n + (p-1)**n = (1+p-1)*(i**n) -> modp = 0 のかずをかける
    ans += powc[i] * powc[(p - i) % p] * powc[0]
    # modp=1となるのはその他のmodp>1となるかずと同じ
    # https://tsuzu.hateblo.jp/entry/2017/02/17/014623
    ans += powc[i] * powc[(p + 1 - i) % p] * powc[1] * (l - 1)
print(ans)