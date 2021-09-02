from sys import argv
from testcase import TestCase


def usage():
    print("python judge.py [testdata_file_path] [output_file_path]")


def judge(tc, output):
    if len(output) != tc.N:
        raise RuntimeError("[ERROR] 出力が%d行ではありません" % (tc.N,))

    for i, row in enumerate(output):
        if len(row) != tc.N:
            raise RuntimeError("[ERROR] %d行目 出力が%d個ではありません" % (i + 1, tc.N))
        for j in range(tc.N):
            if row[j] < 0 or tc.N < row[j]:
                raise RuntimeError("[ERROR] (%d, %d) 出力が不正です : %d" % (i, j, row[j]))

    score = 0
    for i in range(tc.N):
        for j in range(tc.N):
            if output[i][j] == 0:
                continue
            for y in range(i - output[i][j], i + output[i][j] + 1):
                if y < 0 or y >= tc.N:
                    continue
                w = output[i][j] - abs(i - y)
                for x in range(j - w, j + w + 1):
                    if x < 0 or x >= tc.N:
                        continue
                    if (y != i or x != j) and output[y][x] != 0:
                        raise RuntimeError("[ERROR] (%d, %d) は (%d, %d) からの動作音の影響を受ける位置です" % (y, x, i, j))
            score += output[i][j] * tc.E[i][j]

    return score


if __name__ == '__main__':
    if len(argv) < 3:
        usage()
        exit(1)
    with open(argv[1]) as in_file:
        tc = TestCase(input=in_file)
    with open(argv[2]) as out_file:
        output = []
        for i, row in enumerate(out_file, start=1):
            try:
                output.append(list(map(int, row.split())))
            except Exception:
                raise RuntimeError("[ERROR] %d行目 出力が不正です : %s" % (i, row))
    score = judge(tc, output)
    print("score:%d" % score)
