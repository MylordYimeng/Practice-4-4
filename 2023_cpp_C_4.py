from queue import deque

MOD = 998244353
n, m, b, a= map(int, input().split())
mart = [list(map(int, input().split())) for _ in range(n)]

def get_max_min(mart, k, flag): # flag为1得到最大值, -1得到最小值
    ans = []
    for vec in mart:
        temp = []
        dq = deque()
        for i, x in enumerate(vec):
            while dq and flag * x >= flag * vec[dq[-1]]:
                dq.pop()
            dq.append(i) # 存入下标
            if i - dq[0] >= k:
                dq.popleft()
            if i >= k - 1:
                temp.append(vec[dq[0]])
        ans.append(temp)
    return ans

max_row = get_max_min(mart, a, 1)
min_row = get_max_min(mart, a, -1) # 求出各行的最大值
max_col = get_max_min(list(map(list, zip(*max_row))), b, 1)
min_col = get_max_min(list(map(list, zip(*min_row))), b, -1) # 转置传进去

print(sum((x * y) % MOD for row1, row2 in zip(max_col, min_col) for x, y in zip(row1, row2)) % MOD)




