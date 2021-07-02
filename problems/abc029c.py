N = int(input())
s = ["" for i in range(3 ** N)]
# もじすうi
for i in range(N):
    # j*k 1回の文字数
    j = -1
    while j < (3 ** N) - 1:
        for char in ["a", "b", "c"]:
            j += 1
            s[j] += char
    s.sort()
for a in s:
    print(a)
