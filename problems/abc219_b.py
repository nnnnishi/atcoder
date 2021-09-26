d = {}
for i in range(3):
    S = input()
    d[str(i + 1)] = S
ans = ""
T = list(input())
for t in T:
    ans += d[t]
print(ans)
