N, K = map(int, input().split())
S = input()
best = sorted(S)

ans = ""
count = 0
for i in range(N):
    for c in best:
        tmp = 0
        # 辞書順と一致しない
        if S[i] != c:
            # 一致しない数+=1
            tmp += 1
        t = best[:]
        t.remove(c)
        for j in range(i + 1, N):
            if S[j] in t:
                t.remove(S[j])
            else:
                # 一致できない数+=1
                tmp += 1
        # 一致しない数が間に合う
        if tmp + count <= K:
            if S[i] != c:
                # それは動かす
                count += 1
            best.remove(c)
            ans += c
            break

print(ans + S[len(S) :])
