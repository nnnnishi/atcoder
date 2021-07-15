S = list(map(int, input()))
n = len(S)
ones = sum(S)
zeros = n - ones
print(n - abs(ones - zeros))
