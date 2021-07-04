N = int(input())
S = set()
ans = 0
for i in range(1, N + 1):
    if "7" not in set(list(str(i))) and "7" not in set(list(str(format(i, "o")))):
        ans += 1
print(ans)