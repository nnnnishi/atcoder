t, N = list(map(int, input().split()))
# tがちょうどたまる
if (100 / t) * N == (100 / t) * N // 1:
    print((100 * N) // t + N - 1)
# tが毎回ちょうどたまらない
else:
    print((100 * N) // t + N)
