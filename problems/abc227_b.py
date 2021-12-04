N = int(input())
s = [int(_) for _ in input().split()]


def check(x):
    for a in range(1, 340):
        for b in range(1, 340):
            if (4 * a * b + 3 * a + 3 * b) == x:
                return 0
    return 1


ans = 0
for si in s:
    ans += check(si)
print(ans)
