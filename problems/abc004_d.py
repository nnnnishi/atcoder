import networkx as nx

r, g, b = [int(_) for _ in input().split()]
check = set([-100])
G = nx.DiGraph()
G.add_node(-100, demand=-r + 1)
G.add_node(0, demand=-g + 1)
G.add_node(100, demand=-b + 1)

i = 1
while r > 1:
    if -100 + i not in check:
        G.add_edge(-100 + i - 1, -100 + i, weight=1, capacity=1000)
        check.add(-100 + i)
        print(-100 + i - 1, -100 + i)
        if -100 + i not in [-100, 0, 100]:
            r -= 1
            G.add_node(-100 + i, demand=1)
    else:
        if -100 - i not in check:
            G.add_edge(-100 - i + 1, -100 - i, weight=1, capacity=1000)
            check.add(-100 - i)
            print(-100 - i + 1, -100 - i)
            if -100 - i not in [-100, 0, 100]:
                G.add_node(-100 - i, demand=1)
                r -= 1
        else:
            i += 1
print("******")
i = 1
while b > 1:
    if 100 + i not in check:
        G.add_edge(100 + i - 1, 100 + i, weight=1, capacity=1000)
        check.add(100 + i)
        print(100 + i - 1, 100 + i)
        if 100 + i not in [-100, 0, 100]:
            G.add_node(100 + i, demand=1)
            b -= 1
    else:
        if 100 - i not in check:
            G.add_edge(100 - i + 1, 100 - i, weight=1, capacity=1000)
            check.add(100 - i)
            print(100 - i + 1, 100 - i)
            if 100 - i not in [-100, 0, 100]:
                G.add_node(100 - i, demand=1)
                b -= 1
        else:
            i += 1
print("******")
i = 1
check.add(100)
if 99 in check:
    print("YEs")
while g > 1:
    if i not in check:
        G.add_edge(i - 1, i, weight=1, capacity=1000)
        print(i - 1, i)
        check.add(i)
        if i not in [100, 0, -100]:
            g -= 1
            G.add_node(i, demand=1)

    else:
        if -i not in check:
            check.add(-i)
            G.add_edge(-i + 1, -i, weight=1, capacity=1000)
            print(-i + 1, -i)
            if -i not in [100, 0 - 100]:
                G.add_node(-i, demand=1)
                g -= 1
        else:
            i += 1

print(r, b, g)
print(len(check))
flowDict = nx.min_cost_flow(G)
ans = 0
for v in flowDict.values():
    for vv in v.values():
        ans += vv
print(ans)
