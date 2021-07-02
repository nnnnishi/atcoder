from collections import defaultdict

S = list(str(input()))
dic = defaultdict(int)
for s in S:
    dic[s] += 1
ans_list = []
for x in ["A", "B", "C", "D", "E", "F"]:
    ans_list.append(str(dic[x]))
print(" ".join(ans_list))
