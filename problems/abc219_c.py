import string

S = list(input())
d = {}
for i, s in zip(string.ascii_lowercase, S):
    d[s] = i

N = int(input())
num2name = {}
num_l = []
for i in range(N):
    name = input()
    num = ""
    for s in list(name):
        num += d[s]
    num_l.append(num)
    num2name[num] = name

num_l.sort()

for n in num_l:
    print(num2name[n])
