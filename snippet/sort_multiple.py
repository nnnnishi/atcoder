b = [[1, 3], [2, 3], [2, 2]]
b.sort(key=lambda x: (x[0], -x[1]))
print(b)