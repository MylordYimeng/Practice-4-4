to = list(input())
fr = list(input())
n = len(to)
ans = 0
for i in range(n-1):
    if to[i] != fr[i]:
        to[i+1] = '*' if to[i+1] == 'o' else 'o'
        ans += 1
print(ans)
# 当前位置不会再用到, 不用翻
# 简单模拟, 注意在读入的时候把后面的回车也读入进去了, 所以正好不用处理边界 