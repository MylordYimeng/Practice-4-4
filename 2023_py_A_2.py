n = int(input())
std = n // 10
cnt = [0] * 10
cost = [[] for _ in range(10)]
for i in range(n):
    a, b = map(int, input().split())
    cnt[a] += 1
    cost[a].append(b)
    
ans = 0
for i in range(10):
    if cnt[i] > std:
        vec = sorted(cost[i])
        ans += sum(vec[:cnt[i] - std])
print(ans)
