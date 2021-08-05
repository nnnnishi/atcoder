dirstr = "/Users/nnnnishi/codes/atcoder/problems"
contest_num = "213_"
# for char in ["a", "b", "c"]:
for char in ["a", "b", "c", "d", "e", "f", "g", "h"]:
    with open(f"{dirstr}/abc{contest_num}{char}.py", "w") as writer:
        writer.write("N = int(input())\n")
        writer.write("N = list(map(int, input().split()))\n")
