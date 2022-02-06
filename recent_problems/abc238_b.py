N = int(input())
A = list(map(int, input().split()))
L = [0]
t = 0
for a in A:
    t += a
    t %= 360
    L.append(t)
L.sort()

ans = 0
b = 0
for i in range(len(L)):
    ans = max(L[i] - b, ans)
    b = L[i]
ans = max(360 - b, ans)
print(ans)
