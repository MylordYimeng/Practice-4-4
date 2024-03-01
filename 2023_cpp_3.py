import sys

sys.setrecursionlimit(10000)

n = int(input())
son = [[] for _ in range(n+1)]
color = [0] * (n+1)
ans = 0
for i in range(n):
    a, b = map(int, input().split())
    son[b].append(i+1)
    color[i+1] = a
    
def merge(mp, mp2) -> None:
    for key, val in mp2.items():
        if key not in mp:
            mp[key] = val
        else:
            mp[key] += val
    return mp
def dfs(son, color, fa) -> dict:
    global ans
    t = len(son[fa])
    mp = {}
    if t == 0:
        ans += 1
        mp[color[fa]] = 1
        return mp.copy() # leaves

    mp[color[fa]] = 1
    for i in range(t):
        mp2 = dfs(son, color, son[fa][i])
        if len(mp2) <= len(mp):
            mp = merge(mp, mp2)
        else:
            mp = merge(mp2, mp)
        # merge(mp, mp2)
    flag = True
    cmp = mp[color[fa]]
    for _, val in mp.items():
        if val != cmp:
            flag = False
            break
    if flag:
        ans += 1
    return mp.copy()

dfs(son, color, 1)
print(ans)
