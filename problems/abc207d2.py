N = int(input())
S = [complex(*map(int, input().split())) for _ in range(N)]
T = [complex(*map(int, input().split())) for _ in range(N)]

print(S)
print(T)
sumS = sum(S)
sumT = sum(T)

for i in range(N):
    S[i] = S[i] * N - sumS
    T[i] = T[i] * N - sumT
# print(S)
# print(T)
for a in S:  # 0でないaを探して
    if a:
        break

for b in T:  # aをbに重ねた時に
    for s in S:  # 全てのsに重なるtが存在すかを調べる
        for t in T:
            # sとtの長さが同じs*b/a = tを探す
            # Sa->Tb の角度と Ss->Ttの角度が同じもの、かつsとtの長さが同じ
            # 同じのを見つけたら次のs
            print(a, b, s, t, abs(s), abs(t), s * b - t * a)
            if abs(s * b - t * a) <= 10 ** -6 and abs(s) == abs(t):
                break
        # s*b/a = tが見つからなかったので、次のbでトライ
        # breakでぬけなかったとき
        else:
            break
    # 全てのsについて、s*b/a = tが見つかったのでYes!
    # sがbreakでぬけなかったとき
    else:
        print("Yes")
        exit()
print("No")