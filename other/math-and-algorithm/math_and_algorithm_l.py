N = int(input())
for i in range(2, N):
    if i ** 2 >= N:
        print("Yes")
        exit()
    if N % i == 0:
        print("No")
        exit()
