N = int(input())
q = []
for i in range(N):
    q.append([int(_) for _ in input().split()])

ans = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        il, ir = q[i][0], q[i][1]
        jl, jr = q[j][0], q[j][1]
        if jl >= ir:
            continue
        elif il > jr:
            ans += 1
        else:
            p = (ir - il + 1) * (jr - jl + 1)
            # j をスライドさせる
            for k in range(jl, jr + 1):
                if il > k:
                    ans += (ir - il + 1) / p
                elif ir > k >= il:
                    ans += (ir - k) / p
print(ans)