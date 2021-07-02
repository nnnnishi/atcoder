N = list(map(int, input().split()))
if len(set(N)) == 3:
    print(0)
else:
    if N[0] == N[1]:
        print(N[2])
    elif N[0] == N[2]:
        print(N[1])
    else:
        print(N[0])
