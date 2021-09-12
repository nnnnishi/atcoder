import string

d = {}
for i, s in enumerate(string.ascii_lowercase):
    d[i + 1] = s
a = list(map(int, input().split()))
ans = []
for ai in a:
    ans.append(d[ai])
print("".join(ans))
