n = int(input())
nums = list(map(int, input().split()))
ans = 0
for l in range(n):
    mi, ma = nums[l], nums[l]
    for r in range(l, n):
        #ma = max(ma, nums[r])
        #mi = min(mi, nums[r])
        if nums[r] > ma:
            ma = nums[r]
        if nums[r] < mi:
            mi = nums[r]
        # 换成if更快
        if ma - mi + l == r:
            ans += 1
print(ans)
# O(n^2)解法, 蓝桥杯官网能过