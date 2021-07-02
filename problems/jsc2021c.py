A, B = list(map(int, input().split()))
ans = 1
for i in range(2, B - A + 1):
    amari = A % i
    if amari == 0:
        if A + i <= B:
            ans = i
    else:
        if A - amari + 2 * i <= B:
            ans = i

print(ans)