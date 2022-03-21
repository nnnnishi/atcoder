import sys

input = sys.stdin.readline
N, Q = [int(_) for _ in input().split()]
A = [int(_) for _ in input().split()]
move = 0
for _ in range(Q):
    T, x, y = [int(_) for _ in input().split()]
    if T == 1:
        A[(x - 1 - move) % N], A[(y - 1 - move) % N] = (
            A[(y - 1 - move) % N],
            A[(x - 1 - move) % N],
        )
    elif T == 2:
        move += 1
    elif T == 3:
        print(A[(x - 1 - move) % N])
