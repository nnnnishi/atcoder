import string

S = list(input())

for i in list(string.ascii_lowercase):
    if i not in S:
        exit(print(i))
print("None")