from math import pow
n = int(input())
nums = list(map(int, input().split()))
dp = [0] * 10
dp[nums[0] % 10] = 1
for i in range(1, n):
    dp[nums[i]%10] = max(dp[int(nums[i]//pow(10, len(str(nums[i]))-1))] + 1, dp[nums[i]%10])
    # 没必要这样写, 直接当成字符串处理就行
print(n - max(dp))
