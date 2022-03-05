# エラトステネスによる約数の種類（数）の列挙 O(NloglogN)
# https://atcoder.jp/contests/typical90/tasks/typical90_ad
# Nまでで約数の種類がK以上のものを出力

N, K = [int(_) for _ in input().split()]

# iの約数の数 cnt[i]
cnt = [0, 1] + [0] * (N - 1)
for i in range(2, N + 1):
    # 素数でなかったらとばす
    if cnt[i] != 0:
        continue
    # 素数iからiずつ足していく
    for j in range(i, N + 1, i):
        cnt[j] += 1
        """
        素因数の種類でなく数の場合
        tmp = j // i
        while tmp % i == 0:
            cnt[j] += 1
            tmp //= 2
        """
print(cnt)
ans = 0
for n in range(2, N + 1):
    if cnt[n] >= K:
        ans += 1
print(ans)
