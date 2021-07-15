S = list(input())
N = int(input())

l = set()

for i in range(len(S)):
    l.add(S[i])
for i in range(len(S) - 1):
    l.add(S[i] + S[i + 1])
for i in range(len(S) - 2):
    l.add(S[i] + S[i + 1] + S[i + 2])
for i in range(len(S) - 3):
    l.add(S[i] + S[i + 1] + S[i + 2] + S[i + 3])
for i in range(len(S) - 4):
    l.add(S[i] + S[i + 1] + S[i + 2] + S[i + 3] + S[i + 4])
l = list(l)
l.sort()
print(l[N - 1])
