from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

M = int(input())
G = [[] for i in range(9)]
for i in range(M):
    u, v = [int(_) for _ in input().split()]
    u -= 1
    v -= 1
    G[u].append(str(v))
    G[v].append(str(u))

# iがおかれている場所
p = [str(int(_) - 1) for _ in input().split()]


def judge(s, cnt):
    if s == "01234567":
        exit(print(cnt))


# のっていないところiをチェック
def check(ps):
    ps = set(list(ps))
    for i in range(9):
        if str(i) not in ps:
            return i


# なにものっていないiへうごかす
def move(state, cnt):
    check(state)
    # j：iとつながっている場所
    for j in G[i]:
        # p[j]：jにのっているものをiへうごかす
        p[j] = i
        state = "".join(p)
        judge(state, cnt + 1)


cnt = 0
view = set()
states = deque()
add_states = []
state = "".join(p)
states.append(state)
while len(states) > 0:
    while len(states) > 0:
        state = states.popleft()
        if state not in view:
            view.add(state)
            judge(state, cnt)
            # judgeでおわらなければ
            i = check(state)
            # j：iとつながっている場所
            for j in G[i]:
                # p[j]：jにのっているものをiへうごかす
                nx_state = "".join(state.replace(j, str(i)))
                add_states.append(nx_state)
    for s in add_states:
        states.append(s)
    add_states = []
    cnt += 1
print(-1)
