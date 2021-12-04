N, X = [int(_) for _ in input().split()]
A = [int(_) for _ in input().split()]
ans = []
for a in A:
    if a != X:
        ans.append(a)
print(*ans)
