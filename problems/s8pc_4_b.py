N, K = [int(_) for _ in input().split()]
a = [int(_) for _ in input().split()]

ans = 10 ** 30


def has_bit(n, i):
    return (n & 1 << i) > 0


for n in range(1 << (N - 1) + 1):
    before = a[0]
    cnt = 1
    cost = 0
    for i in range(1, N):
        if has_bit(n, i):
            if a[i] - before > 0:
                cnt += 1
                before = a[i]
            else:
                cnt += 1
                cost += before - a[i] + 1
                before = before + 1
                if cost >= ans:
                    break
        else:
            if a[i] > before:
                cnt += 1
                before = a[i]
        if cnt >= K:
            ans = min(cost, ans)
            break
print(ans)
