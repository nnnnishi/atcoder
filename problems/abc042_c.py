N, K = [int(_) for _ in input().split()]
D = set([int(_) for _ in input().split()])
for i in range(N, 10 ** 7):
    if len(D.intersection(set(list(map(int, str(i)))))) == 0:
        exit(print(i))
