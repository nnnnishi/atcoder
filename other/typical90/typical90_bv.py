N = int(input())
S = list(map(int, input().replace("c", "2").replace("b", "1").replace("a", "0")))
print(S)
ans = 0
for i in range(N):
    print(S[i] % 3, S)
    ans += (S[i] % 3) * pow(2, i)
print(ans)
