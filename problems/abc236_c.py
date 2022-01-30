N, M = [int(_) for _ in input().split()]
S = [_ for _ in input().split()]
T = [_ for _ in input().split()]
Tset = set(T)
for s in S:
    if s in Tset:
        print("Yes")
    else:
        print("No")

