N = int(input())
A = list(map(int, input().split()))

cnt = []
for i in range(N):
    cnt.append([-1] * 200)
mod_dic = {}
# さいしょ
cnt[0][A[0] % 200] = 1
mod_dic[A[0] % 200] = [1]


def out(X, Y):
    print("Yes")
    print(len(X), *X, sep=" ")
    print(len(Y), *Y, sep=" ")
    exit()


for idx in range(1, N):
    if A[idx] % 200 in mod_dic:
        # A[idx]とmod_dic[A[idx] % 200]を出力して終わり
        out(mod_dic[A[idx] % 200], [idx + 1])
    else:
        mod_dic[A[idx] % 200] = [idx + 1]
        cnt[idx][A[idx] % 200] = 1

    for m in range(200):
        if cnt[idx - 1][m] != -1:
            if (m + A[idx]) % 200 not in mod_dic:
                cnt[idx][m] = 1
                cnt[idx][(m + A[idx]) % 200] = 1
                mod_dic[(m + A[idx]) % 200] = mod_dic[m] + [idx + 1]
            else:
                out(mod_dic[(m + A[idx]) % 200], mod_dic[m] + [idx + 1])
print("No")