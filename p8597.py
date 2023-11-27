to = list(input())[:-1]
fr = list(input())[:-1]
n = len(to)
diff = []
for i in range(n):
    if to[i] != fr[i]:
        diff.append(i)
n2 = len(diff)
if n2 % 2 == 1:
    print("error") 
ans = 0
for i in range(0,n2,2):
    ans += diff[i+1] - diff[i]
print(ans)
