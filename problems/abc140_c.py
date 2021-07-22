N = int(input())
b = [int(_) for _ in input().split()]
a = [b[N - 2], b[0]]
for i in range(N - 2):
    a.append(min(b[i], b[i + 1]))
print(sum(a))