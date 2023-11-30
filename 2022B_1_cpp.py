orin = input()
size = int(orin[1])
A = [1189, 841]
for _ in range(size):
    if A[0] > A[1]:
        A[0] //= 2
    else:
        A[1] //= 2
if A[0] > A[1]:
    print(A[0])
    print(A[1])
else:
    print(A[1])
    print(A[0])
# 注意大的在前面输出
