a, b, c, d, e, f = [int(_) for _ in input().split()]
# aのはんい
if f % (a * 100) == 0:
    maxa = f // (a * 100)
else:
    maxa = (f // (a * 100)) + 1
if ((f + e) * e) % 100:
    maxc = ((f + e) * e) // 100
else:
    maxc = (((f + e) * e) // 100) + 1
ans = 0
ans_sw = 0
ans_suger = 0
for i in range(maxa):
    for j in range(maxa):
        if i + j == 0:
            continue
        water = a * 100 * i + b * 100 * j
        for k in range(maxc + 1):
            suger = c * k
            if suger + water > f or (suger * 100) / water > e:
                break
            for l in range(maxc + 1):
                suger = c * k + d * l
                if suger + water > f or (suger * 100) / water > e:
                    break
                if (suger * 100) / (suger + water) >= ans:
                    ans = (suger * 100) / (suger + water)
                    ans_sw = suger + water
                    ans_suger = suger
print(ans_sw, ans_suger)