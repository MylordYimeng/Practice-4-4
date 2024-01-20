n, tar = map(int, input().split())
wm = list(map(int, input().split()))
after_sum = wm[:]
after_sum.append(0)
for i in range(n-2, -1, -1):
    after_sum[i] += after_sum[i+1]
ans = 5005
def dfs(pos=0, pri=0.0, times=0):
    global ans
    if times >= ans or pri > tar:
        return
    if tar - pri > after_sum[pos]:
        return
    if pri == tar:
        ans = min(ans, times)
        return
    if pos >= n:
        return
    dfs(pos + 1, pri, times)
    dfs(pos + 1, pri + wm[pos], times)
    dfs(pos + 1, pri + wm[pos]/2, times + 1)
    return 
dfs()
print(-1 if ans == 5005 else ans)