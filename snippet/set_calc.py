# もと
s1 = {"A", "B", "C"}
s2 = {"C", "D", "E"}
print(s1, s2)

print("*" * 20)
# 和集合
u = s1.union(s2)
print(u)

print("*" * 20)
# 共通部分集合
i = s1.intersection(s2)
print(i)
i = s1 & s2
print(i)

print("*" * 20)
# 差集合: 順序により結果が変わる
d1 = s1.difference(s2)
d2 = s2.difference(s1)
print(d1)
print(d2)
d1 = s1 - s2
d2 = s2 - s1
print(d1)
print(d2)

print("*" * 20)
# 包含関係: s1がs2に包含される -> True
s1 = {"A", "B"}
s2 = {"A", "B", "C"}
j1 = s1.issubset(s2)
print(j1)
j1 = s1 <= s2
print(j1)

print("*" * 20)
# 包含関係: s2がs1に包含される -> False
j2 = s2.issubset(s1)
print(j2)
j2 = s2 <= s1
print(j2)

print("*" * 20)
# 要素を削除
print(s1)
s1.remove("A")
print(s1)