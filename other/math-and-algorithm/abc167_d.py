N, K = [int(_) for _ in input().split()]
A = [int(_) for _ in input().split()]
aset = set()
cnt = 0
aset.add(0)
i2c_d = {}
c2i_d = {}
i2c_d[cnt] = 0
c2i_d[0] = cnt
x = A[0] - 1
cnt += 1
while cnt < K:
    if x not in aset:
        # print(cnt, x)
        aset.add(x)
        i2c_d[cnt] = x
        c2i_d[x] = cnt
        x = A[x] - 1
    else:
        res = (K - cnt) % (cnt - c2i_d[x])
        # print("*", res)
        # print((K - cnt), (cnt - c2i_d[x]), cnt)
        print(i2c_d[c2i_d[x] + res] + 1)
        exit()
    cnt += 1
print(x + 1)

