N = int(input())
while N:
    N -= 1
    n = int(input())
    pla = [[] for _ in range(n)]
    for i in range(n):
        pla[i] = list(map(int, input().split()))
    pla = sorted(pla, key=lambda x: x[0])
    do = [False] * n
    flag = False
    def dfs(cur_time):
        if all(do):
            return True
        for i in range(n):
            if not do[i]:
                do[i] = True
                if pla[i][0] > cur_time:
                    if dfs(pla[i][0] + pla[i][2]):
                        return True
                elif cur_time <= pla[i][0] + pla[i][1]:
                    if dfs(cur_time + pla[i][2]):
                        return True
                do[i] = False
        return False
    if dfs(0):
        print("YES")
    else:
        print("NO")
# 如此暴力竟然都过了, 还是用python写C++组的题
        
