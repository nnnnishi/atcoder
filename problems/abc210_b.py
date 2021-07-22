N = int(input())
a = list(map(int, input()))
for i in range(N):
    if a[i] == 1:
        if i % 2 == 0:
            exit(print("Takahashi"))
        else:
            exit(print("Aoki"))
