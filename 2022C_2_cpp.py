n = int(input())
nums = list(map(int, input().split()))
s = sum(nums)
ans = 0
for x in nums:
    s -= x
    ans += x * s
print(ans)
# cpp写可能要考虑整数溢出, python就是秒杀