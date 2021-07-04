N = int(input())
if N % 11 == 0:
    ans = (N // 11) * 2
elif N % 11 > 6:
    ans = (N // 11) * 2 + 2
else:
    ans = (N // 11) * 2 + 1
print(ans)