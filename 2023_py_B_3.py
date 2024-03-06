n = int(input())
s = list(map(int, list(input())))[::-1]
t = list(map(int, list(input())))[::-1]
# 为了方便先反转
ans = 0
dp = [[0,0,0] for _ in range(n)]
dp[0][0] = abs(s[0] - t[0])
dp[0][1] = t[0]+10-s[0]
dp[0][2] = s[0]+10-t[0]
for i in range(1, n):
    
    dp[i][0] = min(dp[i-1][0]+abs(t[i]-s[i]),dp[i-1][1]+abs(t[i]-s[i]-1),dp[i-1][2]+abs(t[i]-s[i]+1))
    dp[i][1] = min(dp[i-1][0]+t[i]+10-s[i],dp[i-1][1]+t[i]+9-s[i],dp[i-1][2]+t[i]+11-s[i])
    dp[i][2] = min(dp[i-1][0]+s[i]+10-t[i],dp[i-1][1]+s[i]+11-t[i],dp[i-1][2]+s[i]+9-t[i])
print(min(dp[n - 1]))
