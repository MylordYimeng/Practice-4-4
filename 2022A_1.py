ans = set()
n = int(input())
i = 2
while i * i <= n:
    if n % i == 0:
        ans.add(i)
        while n % i == 0:
            n /= i # n的因数的质因数一定是n的质因数
    i += 1
print(len(ans) + 1) 
# 固定有个1没算进去
# 质因数分解模板题O(sqrt(N)), 不能全过