#from itertools import permutations as A # 全排列

# nums = [i for i in range(1,10)]
# ans = 0
# n = int(input())
# for x in A(nums):
#     z = 0
#     for i in range(0,8):
#         z = 10*z + x[i]
#         if (z >= n):
#             break
#         a = 0
#         for j in range(i+1, 8):
#             times += 1
#             a = 10 * a + x[j]
#             b = x[j+1]
#             for t in range(j+2, 9):
#                 b = 10 * b + x[t]
#             if (a % b == 0 and a//b + z == n):
#                 ans += 1
# print(times)
# 纯暴力

# n = int(input())
# bit = len(str(n))   # n的位数 
# cnt = 0
# for num in A("123456789"):
#     a, b, c = 0, 0, 0
#     for al in range(bit):
#         t += 1
#         a = 10 * a + int(num[al])
#         temp = n - a 
#         if (a >= n):
#             break;       
#         bLast = temp * int(num[-1]) % 10  #b的尾数，(n-a)c%10        
#         if bLast == 0: 
#             continue
#         bl = num.index(str(bLast))        #根据b的尾数，确定b的长度
#         if bl <= al or bl >= 8: 
#             continue    
#         b = int("".join(num[al+1:bl+1]))
#         c = int("".join(num[bl+1:]))
#         if b % c == 0 and b / c == temp:
#             cnt += 1
# print(cnt)
# 优化了一个for循环, 只能过一个案例, 所以python基本上要求全排列的方法都行不通了

def check(i, ls):
    l1 = list(str(i))
    s1 = list(set(l1))
    return len(l1) == len(s1) and all(x in ls for x in l1)

n = int(input())
l1 = [str(x) for x in range(1,10)]
ans = 0
# n = a + b / c
for a in range(1, n):
    if check(a, l1):
        l2 = l1[:] 
        # l1, l2, l3包含的数字递减
        for x in str(a):
            l2.remove(x)
        for c in range(1, 10**5):
            if not check(c, l2):
                continue
            b = (n - a) * c
            if len(str(b)) + len(str(c)) > len(l2):
                break
            # b递增, 之后情况一定不符合

            l3 = l2[:]
            for x in str(c):
                l3.remove(x)
            if check(b, l3) and len(str(b)) == len(l3):
                ans += 1
print(ans)
