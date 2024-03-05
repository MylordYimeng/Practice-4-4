n = int(input())
l ,r = -1, 1000000005
for i in range(n):
    N, X = map(int, input().split())
    tp_mx = N // X 
    tp_min = N // (X + 1)
    l = max(tp_min, l)
    r = min(tp_mx, r)
print(l + 1, r)