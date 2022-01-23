N = int(input())
A = [int(_) for _ in input().split()]
B = [int(_) for _ in input().split()]

ans = set()
for i, b1 in enumerate(B):
    cand_xor = A[0] ^ b1
    usedB = set()
    usedB.add((i, b1))
    for a in A[1:]:
        ok = False
        for j, b2 in enumerate(B):
            if cand_xor == a ^ b2 and (j, b2) not in usedB:
                ok = True
                usedB.add((j, b2))
                break
        if not ok:
            break
    if ok:
        ans.add(cand_xor)
ans = list(ans)
ans.sort()
print(len(ans))
for a in ans:
    print(a)
