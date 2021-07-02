from itertools import permutations

A = list(str(input()))
B = list(str(input()))
C = list(str(input()))

n_chr = len(set(A + B + C))
if n_chr > 10:
    print("UNSOLVABLE")
else:
    chr2idx = {}
    cnt = 0
    for a in A:
        if a not in chr2idx:
            chr2idx[a] = cnt
            cnt += 1
    for b in B:
        if b not in chr2idx:
            chr2idx[b] = cnt
            cnt += 1
    for c in C:
        if c not in chr2idx:
            chr2idx[c] = cnt
            cnt += 1

    ans = []
    ng = True
    for p in permutations([x for x in range(10)], n_chr):
        if p[chr2idx[A[0]]] == 0 or p[chr2idx[B[0]]] == 0 or p[chr2idx[C[0]]] == 0:
            continue
        a_sum = 0
        for i in range(len(A)):
            a_sum += p[chr2idx[A[i]]] * (10 ** (len(A) - 1 - i))
        b_sum = 0
        for i in range(len(B)):
            b_sum += p[chr2idx[B[i]]] * (10 ** (len(B) - 1 - i))
        c_sum = 0
        for i in range(len(C)):
            c_sum += p[chr2idx[C[i]]] * (10 ** (len(C) - 1 - i))
        if a_sum + b_sum == c_sum:
            print("".join([str(p[chr2idx[A[i]]]) for i in range(len(A))]))
            print("".join([str(p[chr2idx[B[i]]]) for i in range(len(B))]))
            print("".join([str(p[chr2idx[C[i]]]) for i in range(len(C))]))
            ng = False
            break
    if ng:
        print("UNSOLVABLE")