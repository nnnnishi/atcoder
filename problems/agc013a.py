N = int(input())
A = [int(_) for _ in input().split()]
if N == 1:
    print(1)
else:
    i = 0
    cnt = 0
    init = True
    while i < N:
        if init:
            # 仕切り直し
            cnt += 1
            plus = True
            before = A[i]
            is_same = True
            while is_same:
                if i + 1 < N:
                    if A[i + 1] - A[i] == 0:
                        i += 1
                    elif A[i + 1] - A[i] < 0:
                        plus = False
                        is_same = False
                        before = A[i + 1]
                    else:
                        before = A[i + 1]
                        is_same = False
                else:
                    break
            if i + 2 < N:
                i += 2
            else:
                break
        if plus:
            if A[i] - before >= 0:
                before = A[i]
                i += 1
                init = False
            else:
                init = True
        else:
            if A[i] - before <= 0:
                before = A[i]
                i += 1
                init = False
            else:
                init = True
    print(cnt)
