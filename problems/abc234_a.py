def func(t):
    return t ** 2 + 2 * t + 3


t = int(input())
print(func(func(func(t) + t) + func(func(t))))
