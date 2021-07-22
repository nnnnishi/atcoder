L = 10000
N = int(input())
A, B, C = [int(_) for _ in input().split()]
ans = L
for i in range(L):
    if i * A > N:
        break
    for j in range(L):
        if i * A + j * B > N:
            break
        if (N - (A * i + B * j)) % C == 0:
            k = (N - (A * i + B * j)) // C
            ans = min(ans, i + j + k)
print(ans)