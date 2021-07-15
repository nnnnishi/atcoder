A, B = [int(_) for _ in input().split()]
for i in range(100000):
    if (i * 0.08) // 1 == A and (i * 0.1) // 1 == B:
        exit(print(i))
print(-1)
