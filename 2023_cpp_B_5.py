# from bisect import bisect_left
# lim = int(input())
# s, a, b = input().split()
# n = len(s)
# ans = 0
# pre, aft = [], []
# for i in range(n):
#     if s[i] == a:
#         pre.append(i)
#     elif s[i] == b:
#         aft.append(i)
# lpre, laft = len(pre), len(aft)
# for i in range(lpre):
#     index = bisect_left(aft, pre[i] + lim - 1)
#     ans += laft - index
# print(ans)
# O(nlogn) 能过, 但不是最优

lim = int(input())
s, a, b = input().split()
n = len(s)
dp = [0] * n
ans = 0
for i in range(n):
    dp[i] = dp[i - 1]
    if s[i] == a:
        dp[i] += 1 # [0, i]区间内a前缀的数量
    elif s[i] == b and i - lim + 1 >= 0:
        ans += dp[i - lim + 1] # 与这里之前所有a匹配
print(ans)