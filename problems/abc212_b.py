s = list(map(int, list(input())))
if len(set(s)) == 1:
    exit(print("Weak"))
if (s[0] + 1) % 10 == s[1] and (s[1] + 1) % 10 == s[2] and (s[2] + 1) % 10 == s[3]:
    exit(print("Weak"))
print("Strong")
