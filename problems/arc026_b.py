# 素因数分解、試し割り法
# https://qiita.com/drken/items/a14e9af0ca2d857dad23
# O(root(N))
N = int(input())
if N == 1:
    exit(print("Deficient"))
l = [1]
for i in range(2, N):
    if i * i < N:
        if N % i == 0:
            if i != N // i:
                l += [i, N // i]
            else:
                l += [i]
    else:
        break
s = sum(l)
if s == N:
    print("Perfect")
elif s > N:
    print("Abundant")
else:
    print("Deficient")
