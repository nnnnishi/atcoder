N = int(input())
TB, AB = [int(_) for _ in input().split()]
for i in range(N - 1):
    T, A = [int(_) for _ in input().split()]
    bai = 1
    if T < TB:
        bai = -(-TB // T)
    if A < AB:
        bai = max(-(-AB // A), bai)
    TB = bai * T
    AB = bai * A
print(TB + AB)
