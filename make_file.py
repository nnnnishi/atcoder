dirstr = "/Users/nnnnishi/codes/atcoder/recent_problems"
# for char in ["a", "b", "c"]:
for char in ["a", "b", "c", "d", "e", "f"]:
    with open(f"{dirstr}/{char}.py", "w") as writer:
        writer.write("N = int(input())\n")
        writer.write("N = list(map(int, input().split()))\n")
