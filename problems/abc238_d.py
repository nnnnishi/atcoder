T = int(input())
for _ in range(T):
    a, s = list(map(int, input().split()))
    if s >= 2 * a and (s - 2 * a) & a == 0:
        print("Yes")
    else:
        print("No")

