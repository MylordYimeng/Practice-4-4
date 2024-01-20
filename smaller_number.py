num = input()
ans = 0
n = len(num)
for i in range(n):
    for j in range(i+1, n):
        l, r = i, j
        while l < r:
            if num[l] > num[r]:
                ans += 1
                break
            elif num[l] == num[r]:
                l += 1
                r -= 1
            else:
                break
print(ans)