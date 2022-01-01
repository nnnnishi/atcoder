N = int(input())
for _ in range(N):
    S = input()
    ls = len(S)
    if ls % 2 != 0:
        print("NO")
    else:
        if S[0 : ls // 2] == S[ls // 2 :]:
            print("YES")
        else:
            print("NO")
