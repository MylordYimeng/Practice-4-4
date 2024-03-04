def f(s1, s2) -> int:
    n = len(s1)
    ans = 0
    if s1[0] != s2[0] or s1[-1] != s2[-1]:
        return -1
    for i in range(1, n - 1):
        if s1[i] != s2[i]:
            if s1[i - 1] == s1[i + 1] and s1[i + 1] != s1[i]:
                ans += 1
                s1[i] = s2[i]
            else:
                return -1
    if not all(s1[i] == s2[i] for i in range(n)):
        return -1
    return ans

T = int(input())
while T:
    T -= 1
    s1 = list(input())
    s2 = list(input())
    print(f(s2, s1))
# 只有s2可以翻转
