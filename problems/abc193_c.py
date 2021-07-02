N = int(input())

# エラトステネスの篩
# 1はじまりにする、1はTrue、Nまでの配列をつくる
ng = set()
cnt = 0
for n in range(2, N + 1):
    if n not in ng:
        check = n * n
        if check > N:
            break
        while check <= N:
            ng.add(check)
            cnt += 1
            check *= n

# Trueの数を数える
print(N - cnt)
