"""
# メモ
大きなEは生成されにくい


# 方針
1. 市松模様にとる
"""

debug = False

case = 2
if not debug:
    N = int(input())
    E = [[int(_) for _ in input().split()] for i in range(N)]
else:
    with open(f"input_{case}.txt") as reader:
        N = int(reader.readline())
        for i in range(N):
            E = list(map(int, reader.readline().split()))


def main():
    # 4. 出力
    if debug:
        with open(f"output_{case}.txt", "w") as writer:
            for i in range(N):
                for j in range(N):
                    if j < N - 1:
                        writer.write(f"{(i+j)%2} ")
                    if j == N - 1:
                        writer.write(f"{(i+j)%2}\n")

    else:
        # 本番
        for i in range(N):
            for j in range(N):
                if j < N - 1:
                    print((i + j) % 2, end=" ")
                if j == N - 1:
                    print((i + j) % 2)
    return


main()