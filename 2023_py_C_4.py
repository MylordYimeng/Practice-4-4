# 二维差分 + 前缀和
n, m = map(int, input().split())
diff = [[0] * (n + 2) for _ in range(n + 2)]
# 多开两个, 周围围一圈0
for i in range(m):
    a, b, x, y = map(int, input().split())
    diff[a][b] += 1
    diff[x + 1][y + 1] += 1
    diff[a][y + 1] -= 1
    diff[x + 1][b] -= 1
for i in range(n):
    for j in range(n):
        diff[i+1][j+1] += diff[i][j+1] + diff[i+1][j] - diff[i][j]
        print('0' if diff[i+1][j+1]%2 == 0 else '1', end='')
    print()
    
    
