from collections import Counter

_ = int(input())
cnt = Counter(list(map(int,input().split())))
scnt = sorted(cnt.items(), key = lambda x: x[0]) # 按值从小到大排序
scnt += [(x, 0) for x in range(scnt[-1][0] + 1, scnt[-1][0] + 10)] # 防止最后溢出, 多开几个
scnt = [list(vec) for vec in scnt] # Counter.items()是tuple格式,要转成list

i = 0
while True:
    a, t = scnt[i][0], scnt[i][1]
    if t > a and t % (a + 1) == 0:
        scnt[i + 1][1] += t // (a + 1)
        i += 1
        # 如果正好可以凑成一个更大的
    else:
        print(scnt[i][0])
        break
