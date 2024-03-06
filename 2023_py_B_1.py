s = list(input())
s = [ord(x) - ord('a') + 1 for x in s]
n = len(s)
dp = [0] * (n + 1)
dp[0] = s[0]
dp[1] = max(s[0], s[1])
for i in range(2, n):
    dp[i] = max(dp[i - 1], dp[i - 2] + s[i])
print(dp[n - 1])
