N = int(input())
ans = 10 ** 10
for i in range(1, N):
    j = N - i
    ans = min(sum(list(map(int, list(str(i)))) + list(map(int, list(str(j))))), ans)
print(ans)
