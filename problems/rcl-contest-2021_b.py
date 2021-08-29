"""
# メモ
大きなEは生成されにくい


# 方針
1. 市松模様にとる
"""

debug = True

case = 0
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
        
            for i, j in query:
                writer.write(f"{i} {j}\n")

    else:
        # 本番
        for i, j in query:
            print(i, j)
    return





main()