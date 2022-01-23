dirstr = "/Users/nnnnishi/codes/atcoder/recent_problems"
contest_num = "235_"
# for char in ["a", "b", "c"]:
for char in ["a", "b", "c", "d", "e", "f"]:
    with open(f"{dirstr}/abc{contest_num}{char}.py", "w") as writer:
        writer.write("N = int(input())\n")
        writer.write("N = list(map(int, input().split()))\n")
