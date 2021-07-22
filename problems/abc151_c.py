N, M = [int(_) for _ in input().split()]
acset = set()
walist = []
for i in range(M):
    q, s = [_ for _ in input().split()]
    if q not in acset:
        if s == "AC":
            acset.add(q)
        else:
            walist.append(q)
ans_ac = len(acset)
ans_wa = 0
for w in walist:
    if w in acset:
        ans_wa += 1
print(ans_ac, ans_wa)
