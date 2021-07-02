H, W = list(map(int, input().split()))
S = [["."] * (W + 2)]
for y in range(H):
    S.append(["."] + [_ for _ in list(input())] + ["."])
S.append(["."] * (W + 2))

for y in range(1, H + 1):
    for x in range(1, W + 1):
        if (
            S[y][x] == "#"
            and S[y][x + 1] == "."
            and S[y][x - 1] == "."
            and S[y - 1][x] == "."
            and S[y + 1][x] == "."
        ):
            exit(print("No"))
print("Yes")
