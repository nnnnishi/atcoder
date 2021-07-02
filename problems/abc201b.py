N = int(input())
dic = {}
lisT = []
for i in range(N):
    S, T = input().split()
    lisT.append(int(T))
    dic[T] = S
lisT.sort(reverse=True)
print(dic[str(lisT[1])])