N = str(input())
S, T = [_ for _ in input().split()]
print(*[s + t for s, t in zip(S, T)], sep="")
