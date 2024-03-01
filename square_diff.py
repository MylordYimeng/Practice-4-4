l, r = map(int, input().split())
print(sum(int(x % 2 != 0 or x % 4 == 0) for x in range(l, r + 1)))
# n = (x+y)(x-y), 在任何(x, y分别为奇偶)情况下, x+y与x-y都是同奇偶, 即找到两个因数a, b同奇偶
#同时, a, b同奇偶时可以证明x, y有整数解, 奇*奇=奇, 偶*偶=0(mod4)